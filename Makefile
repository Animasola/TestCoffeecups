MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=testingproject.settings $(MANAGE) test testapp

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=testingproject.settings $(MANAGE) syncdb --noinput

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=testingproject.settings $(MANAGE) runserver

migrate:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=testingproject.settings $(MANAGE) migrate testapp
