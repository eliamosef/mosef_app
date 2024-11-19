#!/bin/bash
source ../.venv/bin/activate
export FLASK_APP=../webapp/mosef.py
export FLASK_ENV=development

(cd . ; bash launch.sh >> ../log/data_pipeline.log) &
(cd ../webapp/bin; bash launch-local.sh >> ../../log/webapp.log )
