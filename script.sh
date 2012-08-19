#!/bin/bash

PYTHONPATH='pwd'DJANGO_SETTINGS_MODULE=testingproject.settings django-admin.py models_stat 2>> ./$(date +%Y%m%d).dat;
