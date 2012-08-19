#!/bin/bash

##export DJANGO_SETTINGS_MODULE=testingproject.settings
##export PYTHONPATH=$(pwd)
cd ./testingproject; python manage.py models_stat 2>> ../$(date +%Y%m%d).dat;
