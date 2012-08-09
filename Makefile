MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=kava.settings $(MANAGE) test coffeine

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=kava.settings $(MANAGE) syncdb --noinput

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=kava.settings $(MANAGE) runserver

