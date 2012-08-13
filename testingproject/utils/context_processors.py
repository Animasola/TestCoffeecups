# -*- coding: utf-8 -*-
from django.conf import settings as dset


def django_settings(request):
    return {'django_settings': dset}
