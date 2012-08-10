# -*- coding: utf-8 -*-
from django.views.generic.simple import direct_to_template

from testingproject.testapp.models import MyInfo


def main_page_info(request):

    myinfo = MyInfo.objects.filter()
    return direct_to_template(request, 'main_page.html',
                {'myinfo':myinfo})
