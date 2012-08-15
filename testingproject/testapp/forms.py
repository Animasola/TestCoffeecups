from django import forms
from django.forms import ModelForm

from models import MyInfo


class MyInfoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyInfoForm, self).__init__(*args, **kwargs)
        self.fields['my_photo'].widget.attrs["onchange"] = "upload_img(this);"

    class Media:
        js = ("/static/js/jquery.js",
                "/static/js/jquery.form_3.09.js",)

    class Meta:
        model = MyInfo
