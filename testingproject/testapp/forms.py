from django import forms
from django.forms import ModelForm

from widgets import DatePickerWidget
from models import MyInfo


class MyInfoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyInfoForm, self).__init__(*args, **kwargs)
        self.fields['my_photo'].widget.attrs["onchange"] = "upload_img(this);"
        self.fields['birth_date'].widget = DatePickerWidget(
            params="dateFormat: 'yy-mm-dd', changeYear: true,"
            " defaultDate: '-16y',yearRange: 'c-40:c+16'",
            attrs={'class': 'datepicker', })

    class Media:
        js = ("/static/js/jquery.form_3.09.js",
                "/static/js/form_submit_ajax.js",
                "/static/js/image_refresh.js",)

    class Meta:
        model = MyInfo
