from core_data_modules.cleaners import somali, swahili, Codes
from core_data_modules.traced_data.util.fold_traced_data import FoldStrategies

from configuration import code_imputation_functions
from configuration.code_schemes import CodeSchemes
from src.lib.configuration_objects import CodingConfiguration, CodingModes, CodingPlan


def clean_age_with_range_filter(text):
    """
    Cleans age from the given `text`, setting to NC if the cleaned age is not in the range 10 <= age < 100.
    """
    age = swahili.DemographicCleaner.clean_age(text)
    if type(age) == int and 10 <= age < 100:
        return str(age)
        # TODO: Once the cleaners are updated to not return Codes.NOT_CODED, this should be updated to still return
        #       NC in the case where age is an int but is out of range
    else:
        return Codes.NOT_CODED


def clean_district_if_no_mogadishu_sub_district(text):
    mogadishu_sub_district = somali.DemographicCleaner.clean_mogadishu_sub_district(text)
    if mogadishu_sub_district == Codes.NOT_CODED:
        return somali.DemographicCleaner.clean_somalia_district(text)
    else:
        return Codes.NOT_CODED


S01_RQA_CODING_PLAN = [
        CodingPlan(raw_field="diagnostic_s01e01_raw",
                   time_field="sent_on",
                   run_id_field="diagnostic_s01e01_run_id",
                   coda_filename="COVID19_SOM_s01e01.json",
                   icr_filename="diagnostic_s01e01.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.DIAGNOSTIC_S01E01,
                           coded_field="diagnostic_s01e01_coded",
                           analysis_file_key="diagnostic_s01e01",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.DIAGNOSTIC_S01E01, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 som s01e01"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="diagnostic_s01e02_raw",
                   time_field="sent_on",
                   run_id_field="diagnostic_s01e02_run_id",
                   coda_filename="COVID19_SOM_s01e02.json",
                   icr_filename="diagnostic_s01e02.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.DIAGNOSTIC_S01E02,
                           coded_field="diagnostic_s01e02_coded",
                           analysis_file_key="diagnostic_s01e02",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.DIAGNOSTIC_S01E02, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 som s01e02"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e01_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e01_run_id",
                   coda_filename="IMAQAL_COVID19_s01e01.json",
                   icr_filename="rqa_covid19_mag_s01e01.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E01,
                           coded_field="rqa_covid19_mag_s01e01_coded",
                           analysis_file_key="rqa_covid19_mag_s01e01",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E01, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e01"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e02_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e02_run_id",
                   coda_filename="IMAQAL_COVID19_s01e02.json",
                   icr_filename="rqa_covid19_mag_s01e02.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E02,
                           coded_field="rqa_covid19_mag_s01e02_coded",
                           analysis_file_key="rqa_covid19_mag_s01e02",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E02, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e02"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e03_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e03_run_id",
                   coda_filename="IMAQAL_COVID19_s01e03.json",
                   icr_filename="rqa_covid19_mag_s01e03.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E03,
                           coded_field="rqa_covid19_mag_s01e03_coded",
                           analysis_file_key="rqa_covid19_mag_s01e03",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E03, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e03"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e04_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e04_run_id",
                   coda_filename="IMAQAL_COVID19_s01e04.json",
                   icr_filename="rqa_covid19_mag_s01e04.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E04,
                           coded_field="rqa_covid19_mag_s01e04_coded",
                           analysis_file_key="rqa_covid19_mag_s01e04",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E04, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e04"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e05_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e05_run_id",
                   coda_filename="IMAQAL_COVID19_s01e05.json",
                   icr_filename="rqa_covid19_mag_s01e05.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E05,
                           coded_field="rqa_covid19_mag_s01e05_coded",
                           analysis_file_key="rqa_covid19_mag_s01e05",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E05, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e05"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e06_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e06_run_id",
                   coda_filename="IMAQAL_COVID19_s01e06.json",
                   icr_filename="rqa_covid19_mag_s01e06.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E06,
                           coded_field="rqa_covid19_mag_s01e06_coded",
                           analysis_file_key="rqa_covid19_mag_s01e06",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E06, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e06"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e07_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e07_run_id",
                   coda_filename="IMAQAL_COVID19_s01e07.json",
                   icr_filename="rqa_covid19_mag_s01e07.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E07,
                           coded_field="rqa_covid19_mag_s01e07_coded",
                           analysis_file_key="rqa_covid19_mag_s01e07",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E07, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e07"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e08_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e08_run_id",
                   coda_filename="IMAQAL_COVID19_s01e08.json",
                   icr_filename="rqa_covid19_mag_s01e08.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E08,
                           coded_field="rqa_covid19_mag_s01e08_coded",
                           analysis_file_key="rqa_covid19_mag_s01e08",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E08, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e08"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e09_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e09_run_id",
                   coda_filename="IMAQAL_COVID19_s01e09.json",
                   icr_filename="rqa_covid19_mag_s01e09.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E09,
                           coded_field="rqa_covid19_mag_s01e09_coded",
                           analysis_file_key="rqa_covid19_mag_s01e09",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E09, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e09"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e10_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e10_run_id",
                   coda_filename="IMAQAL_COVID19_s01e10.json",
                   icr_filename="rqa_covid19_mag_s01e10.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E10,
                           coded_field="rqa_covid19_mag_s01e10_coded",
                           analysis_file_key="rqa_covid19_mag_s01e10",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E10, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e10"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e11_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e11_run_id",
                   coda_filename="IMAQAL_COVID19_s01e11.json",
                   icr_filename="rqa_covid19_mag_s01e11.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E11,
                           coded_field="rqa_covid19_mag_s01e11_coded",
                           analysis_file_key="rqa_covid19_mag_s01e11",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E11, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e11"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e12_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e12_run_id",
                   coda_filename="IMAQAL_COVID19_s01e12.json",
                   icr_filename="rqa_covid19_mag_s01e12.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E12,
                           coded_field="rqa_covid19_mag_s01e12_coded",
                           analysis_file_key="rqa_covid19_mag_s01e12",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E12, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e12"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="diagnostic_s01e03_raw",
                   time_field="sent_on",
                   run_id_field="diagnostic_s01e03_run_id",
                   coda_filename="IMAQAL_COVID19_DIAGNOSTIC_s01e03.json",
                   icr_filename="diagnostic_s01e03.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.DIAGNOSTIC_S01E03,
                           coded_field="diagnostic_s01e03_coded",
                           analysis_file_key="diagnostic_s01e03",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.DIAGNOSTIC_S01E03, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value(
                       "imaqal covid19 diagnostic s01e03"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e13_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e13_run_id",
                   coda_filename="IMAQAL_COVID19_s01e13.json",
                   icr_filename="rqa_covid19_mag_s01e13.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E13,
                           coded_field="rqa_covid19_mag_s01e13_coded",
                           analysis_file_key="rqa_covid19_mag_s01e13",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E13, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e13"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e14_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e14_run_id",
                   coda_filename="IMAQAL_COVID19_s01e14.json",
                   icr_filename="rqa_covid19_mag_s01e14.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E14,
                           coded_field="rqa_covid19_mag_s01e14_coded",
                           analysis_file_key="rqa_covid19_mag_s01e14",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E14, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e14"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e15_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e15_run_id",
                   coda_filename="IMAQAL_COVID19_s01e15.json",
                   icr_filename="rqa_covid19_mag_s01e15.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E15,
                           coded_field="rqa_covid19_mag_s01e15_coded",
                           analysis_file_key="rqa_covid19_mag_s01e15",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E15, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e15"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e16_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e16_run_id",
                   coda_filename="IMAQAL_COVID19_s01e16.json",
                   icr_filename="rqa_covid19_mag_s01e16.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E16,
                           coded_field="rqa_covid19_mag_s01e16_coded",
                           analysis_file_key="rqa_covid19_mag_s01e16",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E16, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e16"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e17_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e17_run_id",
                   coda_filename="IMAQAL_COVID19_s01e17.json",
                   icr_filename="rqa_covid19_mag_s01e17.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E17,
                           coded_field="rqa_covid19_mag_s01e17_coded",
                           analysis_file_key="rqa_covid19_mag_s01e17",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E17, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e17"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e18_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e18_run_id",
                   coda_filename="IMAQAL_COVID19_s01e18.json",
                   icr_filename="rqa_covid19_mag_s01e18.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E18,
                           coded_field="rqa_covid19_mag_s01e18_coded",
                           analysis_file_key="rqa_covid19_mag_s01e18",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E18, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e18"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e19_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e19_run_id",
                   coda_filename="IMAQAL_COVID19_s01e19.json",
                   icr_filename="rqa_covid19_mag_s01e19.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E19,
                           coded_field="rqa_covid19_mag_s01e19_coded",
                           analysis_file_key="rqa_covid19_mag_s01e19",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E19, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e19"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e20_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e20_run_id",
                   coda_filename="IMAQAL_COVID19_s01e20.json",
                   icr_filename="rqa_covid19_mag_s01e20.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E20,
                           coded_field="rqa_covid19_mag_s01e20_coded",
                           analysis_file_key="rqa_covid19_mag_s01e20",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E20, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e20"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),
        CodingPlan(raw_field="rqa_covid19_mag_s01e21_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e21_run_id",
                   coda_filename="IMAQAL_COVID19_s01e21.json",
                   icr_filename="rqa_covid19_mag_s01e21.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E21,
                           coded_field="rqa_covid19_mag_s01e21_coded",
                           analysis_file_key="rqa_covid19_mag_s01e21",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E21, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e21"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e22_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e22_run_id",
                   coda_filename="IMAQAL_COVID19_s01e22.json",
                   icr_filename="rqa_covid19_mag_s01e22.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E22,
                           coded_field="rqa_covid19_mag_s01e22_coded",
                           analysis_file_key="rqa_covid19_mag_s01e22",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E22, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e22"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_covid19_mag_s01e23_raw",
                   time_field="sent_on",
                   run_id_field="rqa_covid19_mag_s01e23_run_id",
                   coda_filename="IMAQAL_COVID19_s01e23.json",
                   icr_filename="rqa_covid19_mag_s01e23.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E23,
                           coded_field="rqa_covid19_mag_s01e23_coded",
                           analysis_file_key="rqa_covid19_mag_s01e23",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E23, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01e23"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="imaqal_covid19_s01_closeout_raw",
                   time_field="sent_on",
                   run_id_field="imaqal_covid19_s01_closeout_run_id",
                   coda_filename="IMAQAL_COVID19_s01_closeout.json",
                   icr_filename="imaqal_covid19_s01_closeout.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.IMAQAL_COVID19_S01_CLOSEOUT,
                           coded_field="imaqal_covid19_s01_closeout_coded",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.IMAQAL_COVID19_S01_CLOSEOUT, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s01 closeout"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),
]

S02_RQA_CODING_PLAN = [
    CodingPlan(raw_field="covid19_promo_s02e01_raw",
               time_field="sent_on",
               run_id_field="covid19_promo_s02e01_run_id",
               coda_filename="IMAQAL_COVID19_promo_s02e01.json",
               icr_filename="covid19_promo_s02e01.csv",
               coding_configurations=[
                   CodingConfiguration(
                       coding_mode=CodingModes.MULTIPLE,
                       code_scheme=CodeSchemes.PROMO_S02E01,
                       coded_field="covid19_promo_s02e01_coded",
                       analysis_file_key="covid19_promo_s02e01",
                       fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.PROMO_S02E01, x, y)
                   )
               ],
               ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s02e01 promo"),
               raw_field_fold_strategy=FoldStrategies.concatenate),

    CodingPlan(raw_field="covid19_promo_s02e02_raw",
                   time_field="sent_on",
                   run_id_field="covid19_promo_s02e02_run_id",
                   coda_filename="IMAQAL_COVID19_promo_s02e02.json",
                   icr_filename="covid19_promo_s02e02.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.PROMO_S02E02,
                           coded_field="covid19_promo_s02e02_coded",
                           analysis_file_key="covid19_promo_s02e02",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.PROMO_S02E02, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s02e02 promo"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

    CodingPlan(raw_field="covid19_promo_s02e03_raw",
                       time_field="sent_on",
                       run_id_field="covid19_promo_s02e03_run_id",
                       coda_filename="IMAQAL_COVID19_promo_s02e03.json",
                       icr_filename="covid19_promo_s02e03.csv",
                       coding_configurations=[
                           CodingConfiguration(
                               coding_mode=CodingModes.MULTIPLE,
                               code_scheme=CodeSchemes.PROMO_S02E03,
                               coded_field="covid19_promo_s02e03_coded",
                               analysis_file_key="covid19_promo_s02e03",
                               fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.PROMO_S02E03, x, y)
                           )
                       ],
                       ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s02e03 promo"),
                       raw_field_fold_strategy=FoldStrategies.concatenate),

    CodingPlan(raw_field="rqa_covid19_mag_s02e04_raw",
                       time_field="sent_on",
                       run_id_field="rqa_covid19_mag_s02e04_run_id",
                       coda_filename="IMAQAL_COVID19_s02e04.json",
                       icr_filename="rqa_covid19_mag_s02e04.csv",
                       coding_configurations=[
                           CodingConfiguration(
                               coding_mode=CodingModes.MULTIPLE,
                               code_scheme=CodeSchemes.S02E04,
                               coded_field="rqa_covid19_mag_s02e04_coded",
                               analysis_file_key="rqa_covid19_mag_s02e04",
                               fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S02E04, x, y)
                           )
                       ],
                       ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 s02e04"),
                       raw_field_fold_strategy=FoldStrategies.concatenate),

    CodingPlan(raw_field="vaccination_thoughts_raw",
               time_field="sent_on",
               run_id_field="vaccination_thoughts_run_id",
               coda_filename="IMAQAL_COVID19_vaccination_thoughts.json",
               icr_filename="vaccination_thoughts.csv",
               coding_configurations=[
                   CodingConfiguration(
                       coding_mode=CodingModes.MULTIPLE,
                       code_scheme=CodeSchemes.VACCINATION_THOUGHTS,
                       coded_field="vaccination_thoughts_coded",
                       analysis_file_key="vaccination_thoughts",
                       fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.VACCINATION_THOUGHTS, x, y)
                   )
               ],
               ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 vaccination thoughts"),
               raw_field_fold_strategy=FoldStrategies.concatenate),

    CodingPlan(raw_field="vaccination_thoughts_other_messages_raw",
               time_field="sent_on",
               run_id_field="vaccination_thoughts_other_messages_run_id",
               coda_filename="IMAQAL_COVID19_vaccination_thoughts_other_messages.json",
               icr_filename="vaccination_thoughts_other_messages.csv",
               coding_configurations=[
                   CodingConfiguration(
                       coding_mode=CodingModes.MULTIPLE,
                       code_scheme=CodeSchemes.VACCINATION_THOUGHTS_OTHER_MESSAGES,
                       coded_field="vaccination_thoughts_other_messages_coded",
                       analysis_file_key="vaccination_thoughts_other_messages",
                       fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.VACCINATION_THOUGHTS_OTHER_MESSAGES, x, y)
                   )
               ],
               ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("imaqal covid19 vaccination thoughts other messages"),
               raw_field_fold_strategy=FoldStrategies.concatenate)
]


def get_rqa_coding_plans(pipeline_name):
    if pipeline_name == "IMAQAL_COVID19_s01":
        return S01_RQA_CODING_PLAN
    elif pipeline_name == "IMAQAL_COVID19_s02":
        return S02_RQA_CODING_PLAN
    else:
        assert pipeline_name == "IMAQAL_COVID19_all_seasons"
        return S01_RQA_CODING_PLAN + S02_RQA_CODING_PLAN


def get_demog_coding_plans(pipeline_name):
    return [
        CodingPlan(raw_field="gender_raw",
                   time_field="gender_time",
                   coda_filename="IMAQAL_gender.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.GENDER,
                           cleaner=somali.DemographicCleaner.clean_gender,
                           coded_field="gender_coded",
                           analysis_file_key="gender",
                           fold_strategy=FoldStrategies.assert_label_ids_equal,
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("gender"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal),

        CodingPlan(raw_field="age_raw",
                   time_field="age_time",
                   coda_filename="IMAQAL_age.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.AGE,
                           cleaner=lambda text: clean_age_with_range_filter(text),
                           coded_field="age_coded",
                           analysis_file_key="age",
                           fold_strategy=FoldStrategies.assert_label_ids_equal,
                           include_in_theme_distribution= False
                       ),
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.AGE_CATEGORY,
                           coded_field="age_category_coded",
                           analysis_file_key="age_category",
                           fold_strategy=FoldStrategies.assert_label_ids_equal,
                       )
                   ],
                   code_imputation_function=code_imputation_functions.impute_age_category,
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("age"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal),

        CodingPlan(raw_field="recently_displaced_raw",
                   time_field="recently_displaced_time",
                   coda_filename="IMAQAL_recently_displaced.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.RECENTLY_DISPLACED,
                           cleaner=somali.DemographicCleaner.clean_yes_no,
                           coded_field="recently_displaced_coded",
                           analysis_file_key="recently_displaced",
                           fold_strategy=FoldStrategies.assert_label_ids_equal,
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("recently displaced"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal),

        CodingPlan(raw_field="household_language_raw",
                   time_field="household_language_time",
                   coda_filename="IMAQAL_household_language.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.HOUSEHOLD_LANGUAGE,
                           coded_field="household_language_coded",
                           analysis_file_key="household_language",
                           fold_strategy=FoldStrategies.assert_label_ids_equal,
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("hh language"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal),

        CodingPlan(raw_field="location_raw",
                   time_field="location_time",
                   coda_filename="IMAQAL_location.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.MOGADISHU_SUB_DISTRICT,
                           fold_strategy=FoldStrategies.assert_label_ids_equal,
                           cleaner=somali.DemographicCleaner.clean_mogadishu_sub_district,
                           coded_field="mogadishu_sub_district_coded",
                           analysis_file_key="mogadishu_sub_district",
                           include_in_theme_distribution= False
                       ),
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.SOMALIA_DISTRICT,
                           cleaner=lambda text: clean_district_if_no_mogadishu_sub_district(text),
                           fold_strategy=FoldStrategies.assert_label_ids_equal,
                           coded_field="district_coded",
                           analysis_file_key="district",
                           include_in_theme_distribution= False
                       ),
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.SOMALIA_REGION,
                           fold_strategy=FoldStrategies.assert_label_ids_equal,
                           coded_field="region_coded",
                           analysis_file_key="region",
                       ),
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.SOMALIA_STATE,
                           fold_strategy=FoldStrategies.assert_label_ids_equal,
                           coded_field="state_coded",
                           analysis_file_key="state",
                       ),
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.SOMALIA_ZONE,
                           fold_strategy=FoldStrategies.assert_label_ids_equal,
                           coded_field="zone_coded",
                           analysis_file_key="zone",
                           include_in_theme_distribution= False
                       )
                   ],
                   code_imputation_function=code_imputation_functions.impute_somalia_location_codes,
                   ws_code=CodeSchemes.WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("location"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal)
    ]

def get_follow_up_coding_plans(pipeline_name):
    return []

def get_ws_correct_dataset_scheme(pipeline_name):
    return CodeSchemes.WS_CORRECT_DATASET_SCHEME
