#!/bin/bash

FILE=../../staged_data.csv
dt=$(date +%Y-%m-%d-%H-%M-%S)

if test -f "$FILE"; then
  echo "$FILE exists. Launching integration"
  bash run.sh
  echo "Data integration succeeded"
  mv $FILE ../../archived/staged/staged_data.csv.$dt
else
  echo "No raw file detected"
fi
