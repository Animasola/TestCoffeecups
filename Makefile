MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=testingproject.settings $(MANAGE) test testap

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=testingproject.settings $(MANAGE) syncdb --noinput

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=testingproject.settings $(MANAGE) runserver

