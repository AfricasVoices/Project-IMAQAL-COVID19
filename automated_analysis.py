import argparse
import csv
import glob
import itertools
import shutil
from collections import OrderedDict
import sys

from core_data_modules.analysis import AnalysisConfiguration, engagement_counts, theme_distributions, \
    repeat_participations, sample_messages, traffic_analysis, analysis_utils, traffic_analysis
from core_data_modules.analysis.mapping import participation_maps, somalia_mapper
from core_data_modules.cleaners import Codes
from core_data_modules.data_models.code_scheme import CodeTypes
from core_data_modules.logging import Logger
from core_data_modules.traced_data.io import TracedDataJsonIO
from core_data_modules.util import IOUtils
from dateutil.parser import isoparse

from configuration.code_schemes import CodeSchemes
from src.lib.configuration_objects import CodingModes
from src.lib.pipeline_configuration import PipelineConfiguration

log = Logger(__name__)

IMG_SCALE_FACTOR = 10  # Increase this to increase the resolution of the outputted PNGs
CONSENT_WITHDRAWN_KEY = "consent_withdrawn"
SENT_ON_KEY = "sent_on"


def coding_plans_to_analysis_configurations(coding_plans):
    analysis_configurations = []
    for plan in coding_plans:
        for cc in plan.coding_configurations:
            if not cc.include_in_theme_distribution:
                continue

            analysis_configurations.append(
                AnalysisConfiguration(cc.analysis_file_key, plan.raw_field, cc.coded_field, cc.code_scheme)
            )
    return analysis_configurations


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Runs automated analysis over the outputs produced by "
                                                 "`generate_outputs.py`, and optionally uploads the outputs to Drive.")

    parser.add_argument("user", help="User launching this program")
    parser.add_argument("pipeline_configuration_file_path", metavar="pipeline-configuration-file",
                        help="Path to the pipeline configuration json file")

    parser.add_argument("messages_json_input_path", metavar="messages-json-input-path",
                        help="Path to a JSONL file to read the TracedData of the messages data from")
    parser.add_argument("individuals_json_input_path", metavar="individuals-json-input-path",
                        help="Path to a JSONL file to read the TracedData of the messages data from")
    parser.add_argument("automated_analysis_output_dir", metavar="automated-analysis-output-dir",
                        help="Directory to write the automated analysis outputs to")

    args = parser.parse_args()

    user = args.user
    pipeline_configuration_file_path = args.pipeline_configuration_file_path

    messages_json_input_path = args.messages_json_input_path
    individuals_json_input_path = args.individuals_json_input_path
    automated_analysis_output_dir = args.automated_analysis_output_dir

    IOUtils.ensure_dirs_exist(automated_analysis_output_dir)
    IOUtils.ensure_dirs_exist(f"{automated_analysis_output_dir}/maps/regions")
    IOUtils.ensure_dirs_exist(f"{automated_analysis_output_dir}/maps/districts")
    IOUtils.ensure_dirs_exist(f"{automated_analysis_output_dir}/maps/mogadishu")
    IOUtils.ensure_dirs_exist(f"{automated_analysis_output_dir}/graphs")

    log.info("Loading Pipeline Configuration File...")
    with open(pipeline_configuration_file_path) as f:
        pipeline_configuration = PipelineConfiguration.from_configuration_file(f)
    Logger.set_project_name(pipeline_configuration.pipeline_name)
    log.debug(f"Pipeline name is {pipeline_configuration.pipeline_name}")

    sys.setrecursionlimit(30000)
    # Read the messages dataset
    log.info(f"Loading the messages dataset from {messages_json_input_path}...")
    with open(messages_json_input_path) as f:
        messages = TracedDataJsonIO.import_jsonl_to_traced_data_iterable(f)
        for i in range(len(messages)):
            messages[i] = dict(messages[i].items())
    log.info(f"Loaded {len(messages)} messages")

    # Read the individuals dataset
    log.info(f"Loading the individuals dataset from {individuals_json_input_path}...")
    with open(individuals_json_input_path) as f:
        individuals = TracedDataJsonIO.import_jsonl_to_traced_data_iterable(f)
        for i in range(len(individuals)):
            individuals[i] = dict(individuals[i].items())
    log.info(f"Loaded {len(individuals)} individuals")

    def coding_plans_to_analysis_configurations(coding_plans):
        analysis_configurations = []
        for plan in coding_plans:
            for cc in plan.coding_configurations:
                if not cc.include_in_theme_distribution:
                    continue

                analysis_configurations.append(
                    AnalysisConfiguration(cc.analysis_file_key, plan.raw_field, cc.coded_field, cc.code_scheme)
                )
        return analysis_configurations


    log.info("Computing engagement counts...")
    with open(f"{automated_analysis_output_dir}/engagement_counts.csv", "w") as f:
        engagement_counts.export_engagement_counts_csv(
            messages, individuals, CONSENT_WITHDRAWN_KEY,
            coding_plans_to_analysis_configurations(PipelineConfiguration.RQA_CODING_PLANS),
            f
        )

    log.info("Computing demographic distributions...")
    with open(f"{automated_analysis_output_dir}/demographic_distributions.csv", "w") as f:
        theme_distributions.export_theme_distributions_csv(
            individuals, CONSENT_WITHDRAWN_KEY,
            coding_plans_to_analysis_configurations(PipelineConfiguration.DEMOG_CODING_PLANS),
            [],
            f
        )

    log.info("Computing theme distributions...")
    with open(f"{automated_analysis_output_dir}/theme_distributions.csv", "w") as f:
        theme_distributions.export_theme_distributions_csv(
            individuals, CONSENT_WITHDRAWN_KEY,
            coding_plans_to_analysis_configurations(PipelineConfiguration.RQA_CODING_PLANS),
            coding_plans_to_analysis_configurations(PipelineConfiguration.SURVEY_CODING_PLANS),
            f
        )

    log.info("Computing repeat participations...")
    with open(f"{automated_analysis_output_dir}/repeat_participations.csv", "w") as f:
        repeat_participations.export_repeat_participations_csv(
            individuals, CONSENT_WITHDRAWN_KEY,
            coding_plans_to_analysis_configurations(PipelineConfiguration.RQA_CODING_PLANS),
            f
        )

    # Export raw messages labelled with Meta impact, gratitude and about conversation programmatically known as impact/success story
    log.info("Exporting success story raw messages for each episode...")
    success_story_string_values = ["gratitude", "about_conversation", "impact"]
    with open(f"{automated_analysis_output_dir}/impact_messages.csv", "w") as f:
        sample_messages.export_sample_messages_csv(
            messages, CONSENT_WITHDRAWN_KEY,
            coding_plans_to_analysis_configurations(PipelineConfiguration.RQA_CODING_PLANS),
            f, filter_code_ids=success_story_string_values, limit_per_code=sys.maxsize
        )
    log.info(f"Exporting participation maps for each Somalia region...")
    participation_maps.export_participation_maps(
        individuals, CONSENT_WITHDRAWN_KEY,
        coding_plans_to_analysis_configurations(PipelineConfiguration.RQA_CODING_PLANS),
        AnalysisConfiguration("region", "location_raw", "region_coded", CodeSchemes.SOMALIA_REGION),
        somalia_mapper.export_somalia_region_frequencies_map,
        f"{automated_analysis_output_dir}/maps/regions/regions_",
        export_by_theme=pipeline_configuration.automated_analysis.generate_region_theme_distribution_maps
    )

    log.info(f"Exporting participation maps for each Somalia district...")
    participation_maps.export_participation_maps(
        individuals, CONSENT_WITHDRAWN_KEY,
        coding_plans_to_analysis_configurations(PipelineConfiguration.RQA_CODING_PLANS),
        AnalysisConfiguration("district", "location_raw", "district_coded", CodeSchemes.SOMALIA_DISTRICT),
        somalia_mapper.export_somalia_district_frequencies_map,
        f"{automated_analysis_output_dir}/maps/districts/districts_",
        export_by_theme=pipeline_configuration.automated_analysis.generate_district_theme_distribution_maps
    )

    log.info(f"Exporting participation maps for each Mogadishu sub-district...")
    participation_maps.export_participation_maps(
        individuals, CONSENT_WITHDRAWN_KEY,
        coding_plans_to_analysis_configurations(PipelineConfiguration.RQA_CODING_PLANS),
        AnalysisConfiguration("mogadishu_sub_district", "location_raw", "mogadishu_sub_district_coded", CodeSchemes.MOGADISHU_SUB_DISTRICT),
        somalia_mapper.export_mogadishu_sub_district_frequencies_map,
        f"{automated_analysis_output_dir}/maps/mogadishu/mogadishu_",
        export_by_theme=pipeline_configuration.automated_analysis.generate_mogadishu_theme_distribution_maps
    )

    log.info("automated analysis python script complete")
