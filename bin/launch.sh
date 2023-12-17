#!/bin/bash

while true
  do
    echo "Downloading data"
    cd ../data_collector/bin
    bash get_data.sh && echo "Data downloaded" && echo "Integrating data" && cd ../../data_integrator/bin &&  bash workflow.sh && echo "Data integrated" &&  echo "Processing data" && cd ../../data_processor/bin && bash workflow.sh && echo "Processing data" && cd ../../bin && echo "Data processing succeeded"
  done
