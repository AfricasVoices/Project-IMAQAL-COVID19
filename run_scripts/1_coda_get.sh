#!/usr/bin/env bash

set -e

if [[ $# -ne 3 ]]; then
    echo "Usage: ./1_coda_get.sh <coda-auth-file> <coda-v2-root> <data-root>"
    echo "Downloads coded messages datasets from Coda to '<data-root>/Coded Coda Files'"
    exit
fi

AUTH=$1
CODA_V2_ROOT=$2
DATA_ROOT=$3

./checkout_coda_v2.sh "$CODA_V2_ROOT"

DATASETS=(
    "COVID19_SOM_s01e01"
    "COVID19_SOM_s01e02"
    "IMAQAL_COVID19_s01e01"
    "IMAQAL_COVID19_s01e02"
    "IMAQAL_COVID19_s01e03"
    "IMAQAL_COVID19_s01e04"
    "IMAQAL_COVID19_s01e05"
    "IMAQAL_COVID19_s01e06"
    "IMAQAL_COVID19_s01e07"
    "IMAQAL_COVID19_s01e08"
    "IMAQAL_COVID19_s01e09"
    "IMAQAL_COVID19_s01e10"
    "IMAQAL_COVID19_s01e11"
    "IMAQAL_COVID19_s01e12"
    "IMAQAL_COVID19_DIAGNOSTIC_s01e03"
    "IMAQAL_COVID19_s01e13"
    "IMAQAL_COVID19_s01e14"
    "IMAQAL_COVID19_s01e15"
    "IMAQAL_COVID19_s01e16"
    "IMAQAL_COVID19_s01e17"
    "IMAQAL_COVID19_s01e18"
    "IMAQAL_COVID19_s01e19"
    "IMAQAL_COVID19_s01e20"
    "IMAQAL_COVID19_s01e21"
    "IMAQAL_COVID19_s01e22"
    "IMAQAL_COVID19_s01e23"

    "IMAQAL_gender"
    "IMAQAL_location"
    "IMAQAL_age"
    "IMAQAL_recently_displaced"
    "IMAQAL_household_language"
)

cd "$CODA_V2_ROOT/data_tools"
git checkout "e895887b3abceb63bab672a262d5c1dd73dcad92"  # (master which supports incremental get)

mkdir -p "$DATA_ROOT/Coded Coda Files"

for DATASET in ${DATASETS[@]}
do
    FILE="$DATA_ROOT/Coded Coda Files/$DATASET.json"

    if [ -e "$FILE" ]; then
        echo "Getting messages data from ${DATASET} (incremental update)..."
        MESSAGES=$(pipenv run python get.py --previous-export-file-path "$FILE" "$AUTH" "${DATASET}" messages)
        echo "$MESSAGES" >"$FILE"
    else
        echo "Getting messages data from ${DATASET} (full download)..."
        pipenv run python get.py "$AUTH" "${DATASET}" messages >"$FILE"
    fi

done
