# -*- coding: utf-8 -*-
from django.views.generic.simple import direct_to_template

from testingproject.testapp.models import MyInfo, ReqsHistory


def main_page_info(request):

    myinfo = MyInfo.objects.filter()
    return direct_to_template(request, 'main_page.html',
                {'myinfo': myinfo})


def requests_log(request):
    first_ten_requests =\
            ReqsHistory.objects.filter().order_by('timestamp')[: 10]
    return direct_to_template(request, "reqs_log.html",
                {'requests': first_ten_requests}
            )
