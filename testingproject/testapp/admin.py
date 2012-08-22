from django.contrib import admin
from testingproject.testapp.models import MyInfo, ModelLog


class MyInfoAdmin(admin.ModelAdmin):
     list_display = ('name', 'surname', 'birth_date', 'email', 'other_cont', )


class ModelLogAdmin(admin.ModelAdmin):
     list_display = ('model', 'target_instance', 'action', 'change_timestamp', )
     list_filter = ('model', 'action', 'change_timestamp', )
     search_fields = ['model']


admin.site.register(MyInfo, MyInfoAdmin)
admin.site.register(ModelLog, ModelLogAdmin)
