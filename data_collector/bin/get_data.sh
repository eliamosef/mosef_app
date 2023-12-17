#!/bin/bash
source ../conf/collector.conf

echo "Form ID is set as: ${form_id}"
echo "Target path is set as: ${target_path}"

curl -XGET https://docs.google.com/spreadsheets/d/${form_id}/gviz/tq?tqx=out:csv > ${target_path}/raw_data.csv
