MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=TestCoffecups.settings $(MANAGE) test testapp

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=TestCoffecups.settings $(MANAGE) syncdb --noinput

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=TestCoffecups.settings $(MANAGE) runserver

