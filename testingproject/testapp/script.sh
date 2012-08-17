#!/bin/bash
clear

python manage.py models_stat 2>> ./script_folder/$(date +%Y%m%d).dat
echo
