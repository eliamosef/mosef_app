#!/bin/bash

(cd . ; bash launch.sh >> ../log/data_pipeline.log) &
(cd ../webapp/bin; bash launch.sh >> ../../log/webapp.log )