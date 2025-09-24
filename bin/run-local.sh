#!/bin/bash
source ../.venv/Scripts/activate
export FLASK_APP=../webapp/mosef.py
export FLASK_ENV=development

(cd ../webapp/bin; bash launch-local.sh >> ../../log/webapp.log ) &
(cd . ; bash launch-local.sh >> ../log/data_pipeline.log)
wait
