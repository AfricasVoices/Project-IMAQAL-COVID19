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

    "IMAQAL_gender"
    "IMAQAL_location"
    "IMAQAL_age"
    "IMAQAL_recently_displaced"
    "IMAQAL_household_language"
)

cd "$CODA_V2_ROOT/data_tools"
git checkout "94a55d9218fb072ef2c15ee2c27c4214b036bd2f"  # (master which supports LastUpdated)

mkdir -p "$DATA_ROOT/Coded Coda Files"

for DATASET in ${DATASETS[@]}
do
    echo "Getting messages data from ${DATASET}..."

    pipenv run python get.py "$AUTH" "${DATASET}" messages >"$DATA_ROOT/Coded Coda Files/$DATASET.json"
done
