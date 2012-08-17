from django.contrib import admin
from testingproject.testapp.models import MyInfo


class MyInfoAdmin(admin.ModelAdmin):
     list_display = ('name', 'surname', 'birth_date', 'email', 'other_cont', )



admin.site.register(MyInfo, MyInfoAdmin)
