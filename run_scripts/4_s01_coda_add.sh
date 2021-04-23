#!/usr/bin/env bash

set -e

if [[ $# -ne 3 ]]; then
    echo "Usage: ./4_all_seasons_coda_add.sh <coda-auth-file> <coda-v2-root> <data-root>"
    echo "Uploads coded messages datasets from '<data-root>/Outputs/Coda Files' to Coda"
    exit
fi

AUTH=$1
CODA_V2_ROOT=$2
DATA_ROOT=$3

./checkout_coda_v2.sh "$CODA_V2_ROOT"

DATASETS=(
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
    "IMAQAL_COVID19_s01_closeout"
    "IMAQAL_COVID19_promo_s02e01"
    "IMAQAL_COVID19_promo_s02e02"
    "IMAQAL_COVID19_promo_s02e03"
    "IMAQAL_COVID19_s02e04"

    "IMAQAL_gender"
    "IMAQAL_location"
    "IMAQAL_age"
    "IMAQAL_recently_displaced"
    "IMAQAL_household_language"
)

cd "$CODA_V2_ROOT/data_tools"
git checkout "c47977d03f96ba3e97c704c967c755f0f8b666cb"  # (master which supports incremental add)

for DATASET in ${DATASETS[@]}
do
    MESSAGES_TO_ADD="$DATA_ROOT/Outputs/Coda Files/$DATASET.json"
    PREVIOUS_EXPORT="$DATA_ROOT/Coded Coda Files/$DATASET.json"

    if [ -e "$MESSAGES_TO_ADD" ]; then  # Stop-gap workaround for supporting multiple pipelines until we have a Coda library
        if [ -e "$PREVIOUS_EXPORT" ]; then
            echo "Pushing messages data to ${DATASET} (with incremental get)..."
            pipenv run python add.py --previous-export-file-path "$PREVIOUS_EXPORT" "$AUTH" "${DATASET}" messages "$MESSAGES_TO_ADD"
        else
            echo "Pushing messages data to ${DATASET} (with full download)..."
            pipenv run python add.py "$AUTH" "${DATASET}" messages "$MESSAGES_TO_ADD"
        fi
    fi
done
