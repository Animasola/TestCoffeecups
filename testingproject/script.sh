#!/bin/bash

##DJANGO_SETTINGS_MODULE=testingproject.settings
python manage.py models_stat 2>> ./$(date +%Y%m%d).dat


##export PYTHONPATH=${PYTHONPATH}:$(pwd)/script.sh
##models_stat
##	PYTHONPATH='pwd' DJANGO_SETTINGS_MODULE=testingproject.settings $(MANAGE) python $com_ 2>> ./$(date +%Y%m%d).dat
