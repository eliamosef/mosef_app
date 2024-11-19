#!/bin/bash

(cd . ; bash launch.sh >> ../log/data_pipeline.log) &
(cd ../webapp/bin; bash launch-local.sh >> ../../log/webapp.log )
