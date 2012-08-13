# -*- coding: utf-8 -*-
from django.views.generic.simple import direct_to_template

from testingproject.testapp.models import MyInfo, ReqsHistory
from forms import MyInfoForm


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


def edit_my_info(request):
    try:
        my_info = MyInfo.objects.get(pk=1)
    except:
        my_info = None
    if request.method == 'POST':
        form = MyInfoForm(request.POST, request.FILES, instance=my_info)
        if form.is_valid():
            form.save()
    else:
        form = MyInfoForm(instance=my_info)
    return direct_to_template(request, 'edit_my_info.html',
                {'form': form})
