import json

from core_data_modules.data_models import CodeScheme


def _open_scheme(filename):
    with open(f"code_schemes/{filename}", "r") as f:
        firebase_map = json.load(f)
        return CodeScheme.from_firebase_map(firebase_map)


class CodeSchemes(object):
    DIAGNOSTIC_S01E01 = _open_scheme("diagnostic_s01e01.json")
    DIAGNOSTIC_S01E02 = _open_scheme("diagnostic_s01e02.json")
    DIAGNOSTIC_S01E03 = _open_scheme("diagnostic_s01e03.json")
    S01E01 = _open_scheme("s01e01.json")
    S01E02 = _open_scheme("s01e02.json")
    S01E03 = _open_scheme("s01e03.json")
    S01E04 = _open_scheme("s01e04.json")
    S01E05 = _open_scheme("s01e05.json")
    S01E06 = _open_scheme("s01e06.json")
    S01E07 = _open_scheme("s01e07.json")
    S01E08 = _open_scheme("s01e08.json")
    S01E09 = _open_scheme("s01e09.json")
    S01E10 = _open_scheme("s01e10.json")
    S01E11 = _open_scheme("s01e11.json")
    S01E12 = _open_scheme("s01e12.json")
    S01E13 = _open_scheme("s01e13.json")
    S01E14 = _open_scheme("s01e14.json")
    S01E15 = _open_scheme("s01e15.json")
    S01E16 = _open_scheme("s01e16.json")
    S01E17 = _open_scheme("s01e17.json")
    S01E18 = _open_scheme("s01e18.json")
    S01E19 = _open_scheme("s01e19.json")
    S01E20 = _open_scheme("s01e20.json")
    S01E21 = _open_scheme("s01e21.json")
    S01E22 = _open_scheme("s01e22.json")
    S01E23 = _open_scheme("s01e23.json")
    IMAQAL_COVID19_S01_CLOSEOUT = _open_scheme("imaqal_covid19_s01_closeout.json")

    S02E01 = _open_scheme("s02e01.json")
    S02E02 = _open_scheme("s02e02.json")
    S02E03 = _open_scheme("s02e03.json")
    S02E04 = _open_scheme("s02e04.json")

    AGE = _open_scheme("age.json")
    AGE_CATEGORY = _open_scheme("age_category.json")
    RECENTLY_DISPLACED = _open_scheme("recently_displaced.json")
    HOUSEHOLD_LANGUAGE = _open_scheme("household_language.json")
    GENDER = _open_scheme("gender.json")

    SOMALIA_OPERATOR = _open_scheme("somalia_operator.json")
    SOMALIA_DISTRICT = _open_scheme("somalia_district.json")
    MOGADISHU_SUB_DISTRICT = _open_scheme("mogadishu_sub_district.json")
    SOMALIA_REGION = _open_scheme("somalia_region.json")
    SOMALIA_STATE = _open_scheme("somalia_state.json")
    SOMALIA_ZONE = _open_scheme("somalia_zone.json")

    WS_CORRECT_DATASET_SCHEME = _open_scheme("ws_correct_dataset.json")
