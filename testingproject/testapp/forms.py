from django import forms
from django.forms import ModelForm

from models import MyInfo


class MyInfoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyInfoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = MyInfo
