from django.db import models
from django.db.models import get_models
from django.db.models.signals import post_save, post_delete
from signals import ModelChangeLog


class MyInfo(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    surname = models.CharField(max_length=75, verbose_name='Last name')
    birth_date = models.DateField(auto_now=False, auto_now_add=False,
                verbose_name='Date of birth')
    bio = models.TextField(verbose_name='Bio')
    email = models.EmailField(max_length=75, verbose_name='Email')
    jabber = models.CharField(max_length=50, verbose_name='Jabber')
    skype = models.CharField(max_length=50, verbose_name='Skype')
    other_cont = models.TextField()
    my_photo = models.ImageField(upload_to='img/', blank=True, null=True)

    def __unicode__(self):
        return '%s %s' % (self.name, self.surname)


class ReqsHistory(models.Model):
    req_url = models.CharField(max_length=255)
    req_type = models.CharField(max_length=10)
    req_ip = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.req_url


class ModelLog(models.Model):
    model = models.CharField(max_length=30)
    action = models.CharField(max_length=15)
    id_zap = models.IntegerField()
    change_timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return "%s %s %s %s" % (self.model, self.id_zap,
                                self.action, self.change_timestamp)


for idx, model in enumerate(get_models()):
    if model.__name__ != "ModelLog":
        post_save.connect(ModelChangeLog, sender=model, dispatch_uid="%sca%s" % (model.__name__, idx))
        post_delete.connect(ModelChangeLog, sender=model, dispatch_uid="%sd%s" % (model.__name__, idx))
