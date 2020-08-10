import argparse
import csv
import json
import sys

from core_data_modules.logging import Logger
from id_infrastructure.firestore_uuid_table import FirestoreUuidTable
from storage.google_cloud import google_cloud_utils
from core_data_modules.cleaners import Codes


from src.lib import PipelineConfiguration

log = Logger(__name__)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generates a list of phone numbers of consented participants"
                                                 "who participated in the last five episodes, to be used in the weekly "
                                                 "sms advert")

    parser.add_argument("google_cloud_credentials_file_path", metavar="google-cloud-credentials-file-path",
                        help="Path to a Google Cloud service account credentials file to use to access the "
                             "credentials bucket")
    parser.add_argument("pipeline_configuration_file_path", metavar="pipeline-configuration-file",
                        help="Path to Imaqal full pipeline configuration json file")
    parser.add_argument("imaqal_csv_by_individual_input_path", metavar="imaqal-csv-csv-by-individual-output-path",
                        help="Imaqal Analysis dataset where respondents are the unit for analysis (i.e. one respondent "
                             "per row, with all their messages joined into a single cell)")
    parser.add_argument("imaqal_covid19_csv_by_individual_input_path", metavar="imaqal-covid19-csv-csv-by-individual-output-path",
                        help="imaqal_covid19 Analysis dataset where respondents are the unit for analysis (i.e. one respondent "
                             "per row, with all their messages joined into a single cell)")
    parser.add_argument("csv_output_file_path", metavar="csv-output-file-path",
                        help="Path to a CSV file to write the  advert phone numbers to. "
                             "Exported file is in a format suitable for direct upload to Rapid Pro")

    args = parser.parse_args()

    google_cloud_credentials_file_path = args.google_cloud_credentials_file_path
    pipeline_configuration_file_path = args.pipeline_configuration_file_path
    imaqal_csv_by_individual_input_path = args.imaqal_csv_by_individual_input_path
    imaqal_covid19_csv_by_individual_input_path = args.imaqal_covid19_csv_by_individual_input_path

    csv_output_file_path = args.csv_output_file_path

    # Read the settings from the configuration file
    log.info("Loading Pipeline Configuration File...")
    with open(pipeline_configuration_file_path) as f:
        pipeline_configuration = PipelineConfiguration.from_configuration_file(f)
    Logger.set_project_name(pipeline_configuration.pipeline_name)
    log.debug(f"Pipeline name is {pipeline_configuration.pipeline_name}")

    log.info("Downloading Firestore UUID Table credentials...")
    firestore_uuid_table_credentials = json.loads(google_cloud_utils.download_blob_to_string(
        google_cloud_credentials_file_path,
        pipeline_configuration.phone_number_uuid_table.firebase_credentials_file_url
    ))

    phone_number_uuid_table = FirestoreUuidTable(
        pipeline_configuration.phone_number_uuid_table.table_name,
        firestore_uuid_table_credentials,
        "avf-phone-uuid-"
    )
    log.info("Initialised the Firestore UUID table")

    # Fetch for consented uuids in both projects
    advert_uuids = set()
    cohort_conversation = [
  "avf-phone-uuid-efd3d5fa-4bcb-401d-ba98-e26793d2690b",
  "avf-phone-uuid-20a82324-d324-41b5-9300-ebdece656b53",
  "avf-phone-uuid-8b2ed9dc-3b34-4ded-a118-33c3f669d5bd",
  "avf-phone-uuid-4ae51926-3b12-49f9-b97e-74c42b84487d",
  "avf-phone-uuid-501294fc-c49b-4c12-945a-996a71c98a21",
  "avf-phone-uuid-5851921c-9edf-4908-9d7d-ed7d39a3c775",
  "avf-phone-uuid-5fc74270-bb07-41cd-a02b-8a16484edc24",
  "avf-phone-uuid-65f93aa2-44da-4165-b166-91d7f6b193e5",
  "avf-phone-uuid-79d764d7-8e6f-45ad-b015-0db8e6bf4cad",
  "avf-phone-uuid-8344a060-83a3-4594-afbe-7d83c94a5b4d",
  "avf-phone-uuid-8578f0ef-a325-4247-aaf9-b1974dd6c281",
  "avf-phone-uuid-95183343-4816-48aa-b81a-9d5673413a89",
  "avf-phone-uuid-053a33f5-ea34-466d-9f79-bb78dbdc55fb",
  "avf-phone-uuid-2ee7029b-2918-45e3-b5b3-fb99ea2bedcc",
  "avf-phone-uuid-1d7c0871-eb72-4ce3-b6ec-c53ac3cb7da2",
  "avf-phone-uuid-d628e5d4-2114-4db2-be88-6f315fde2f8e",
  "avf-phone-uuid-df3d386e-47d4-45f6-928a-7e0f17c05890",
  "avf-phone-uuid-e7d69832-2acc-4a34-a9d1-5d525d8fd71b",
  "avf-phone-uuid-ecb1be5a-b14e-4647-9d8b-0a05027ed036",
  "avf-phone-uuid-ed31598b-92ba-43e7-bf80-a8bb34de9cc0",
  "avf-phone-uuid-f91d887c-6f24-4e34-b2db-4dfccaa2ce27",
  "avf-phone-uuid-fa267a11-08c1-4cee-a7f8-5ceae4a91b62",
  "avf-phone-uuid-5a376bf8-023b-4c6b-ac54-ec29a95c1603",
  "avf-phone-uuid-8b5c31ae-f0de-4c59-bb4a-331a9ad40a44",
  "avf-phone-uuid-fe233cfe-af49-4456-b05e-aabe31020dfb",
  "avf-phone-uuid-07524892-c6a2-498a-9001-94d28c0d8955",
  "avf-phone-uuid-b83e8fd5-0ed7-4d94-b0d4-f8095877ab1d",
  "avf-phone-uuid-179acf00-86d6-43ea-82ae-3ca16f32686c",
  "avf-phone-uuid-19a6da86-0d0f-445f-86ec-06748118728a",
  "avf-phone-uuid-1e226277-757e-4d6e-9ac8-1fa0f5d0d7d4",
  "avf-phone-uuid-235a8a22-f322-42f9-a517-97adf52c211c",
  "avf-phone-uuid-064b7e22-9608-48e7-872a-aaf706b995cd",
  "avf-phone-uuid-2659fa0a-532d-4268-add8-46d23635b7c0",
  "avf-phone-uuid-27739a4a-b76c-4abb-a91e-fa59f3c53574",
  "avf-phone-uuid-bdf20f40-4325-4daa-9b10-488205fa4921",
  "avf-phone-uuid-6a8d5e68-783f-42b0-9ab8-1e8618609f2e",
  "avf-phone-uuid-7cc4c47b-a23a-4091-8bb9-a2d4c1261819",
  "avf-phone-uuid-9c95f3fb-2cc4-4367-a0e9-8202f77fce7a",
  "avf-phone-uuid-a63db2c0-5a64-479f-84a0-22d53c14531b",
  "avf-phone-uuid-219e39b9-a9b8-4c5f-988b-7a0055156f28",
  "avf-phone-uuid-bc6530be-f3e2-48c4-b6bf-b3bc4a036072",
  "avf-phone-uuid-da45e880-612c-461b-ab8c-4cf666268073",
  "avf-phone-uuid-c9ffff69-f791-4253-85b2-32134a2a466c",
  "avf-phone-uuid-dc7dc489-3b20-42a4-896a-ee9e87458c6d",
  "avf-phone-uuid-f61e0e55-2358-4981-a952-f31bbf1e02a2",
  "avf-phone-uuid-0b6b53fa-96ff-47be-9b57-38060a1c5332",
  "avf-phone-uuid-15659c56-6b55-40d2-8817-e69186cc9290",
  "avf-phone-uuid-1d80c39b-1bb0-419c-b88e-eb4295c7bbfe",
  "avf-phone-uuid-24aa1875-6db8-4ef0-98a2-bdda1ea882dc",
  "avf-phone-uuid-259cf10f-5c6c-4faf-ad2a-70a114ec654a",
  "avf-phone-uuid-8551b302-e48e-48e0-b117-d38764ea7e2d",
  "avf-phone-uuid-ac6f286c-ce66-435e-92c1-1f2938f8f9bc",
  "avf-phone-uuid-afbfecfb-0318-41b7-bf30-5441cc3fc368",
  "avf-phone-uuid-bb995ca4-abe8-4cf0-aad8-0f3a4bdfaac3",
  "avf-phone-uuid-8edbdab0-193c-47d0-8e48-0cb214ba098c",
  "avf-phone-uuid-eda7523f-0984-4bef-9811-486af1b26dee",
  "avf-phone-uuid-f487f2cd-3e63-4004-abad-e9e5da258765",
  "avf-phone-uuid-fab8fd40-4a42-4c12-82dd-3807f51ddfd8",
  "avf-phone-uuid-0a225682-c2a8-40d2-bb7a-658d8987e744",
  "avf-phone-uuid-0c54af7e-18d9-4534-bef7-0230163bc586",
  "avf-phone-uuid-6ab43907-58b3-4906-80f5-783b3e1a43be",
  "avf-phone-uuid-b7c3db4f-018f-4be6-92af-8aedc3769ad2",
  "avf-phone-uuid-bd837f8c-8bb5-4071-9487-22d129e48934",
  "avf-phone-uuid-1639ec69-a06d-4d4b-b307-4cf12c7b49a0",
  "avf-phone-uuid-55c89cff-b8f4-4136-b359-d52d8a4bd496",
  "avf-phone-uuid-6290f209-69b1-493e-b264-627c7328ae78",
  "avf-phone-uuid-e90a0d17-0a93-48cc-9be3-f6caab42378c",
  "avf-phone-uuid-ea4ec87e-6deb-490e-81d3-ab797602a0da",
  "avf-phone-uuid-37687190-21f5-4296-9890-6d2b15157309",
  "avf-phone-uuid-e5ec91e3-4a96-442c-aca5-0840912d1e8a",
  "avf-phone-uuid-365e3c48-1d04-4027-a9d4-99657d033d9f"
]
    '''
    for file in  [imaqal_csv_by_individual_input_path, imaqal_covid19_csv_by_individual_input_path]:
        with open(f"{file}", "r") as csv_file:
            csv.field_size_limit(sys.maxsize)
            data = csv.DictReader(csv_file)
            for ind in data:
                if ind['uid'].startswith('avf'):
                    advert_uuids.add(ind['uid'])

    '''
    # Convert the uuids to phone numbers
    log.info(f'Converting {len(cohort_conversation)} uuids to phone numbers...')
    uuids_to_phone_numbers = phone_number_uuid_table.uuid_to_data_batch(list(cohort_conversation))
    consented_phone_numbers = [f"+{uuids_to_phone_numbers[uuid]}" for uuid in cohort_conversation]
    '''
    # Filter non Hormuud(+25261) and Golis(+25290) phone numbers
    log.info(f'Filtering out non Hormuud(+25261) and Golis(+25290) phone numbers...')
    advert_phone_numbers = set()
    
    
    other_mno_count = 0
    for phone_number in consented_phone_numbers:
        if phone_number.startswith('+25261') or phone_number.startswith('+25290'):
            advert_phone_numbers.add(phone_number)
        else:
            other_mno_count +=1
    log.info(f'Filtered {other_mno_count} phone numbers, returning {len(advert_phone_numbers)} phone numbers...')
    '''

    # Export contacts CSV
    log.warning(f"Exporting {len(consented_phone_numbers)} phone numbers to {csv_output_file_path}...")
    with open(f'{csv_output_file_path}', "w") as f:
        writer = csv.DictWriter(f, fieldnames=["URN:Tel", "Name"], lineterminator="\n")
        writer.writeheader()

        for number in consented_phone_numbers:
            writer.writerow({
                "URN:Tel": number
            })
        log.info(f"Wrote {len(consented_phone_numbers)} contacts to {csv_output_file_path}")
