#!/bin/bash

while true
  do
    echo "Downloading data"
    bash ./get_data.sh
    echo "Data downloaded"
    sleep 5
  done
