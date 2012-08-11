from django.db import models


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

    def __unicode__(self):
        return '%s %s' % (self.name, self.surname)



class ReqsHistory(models.Model):
    req_url = models.CharField(max_length=255)
    req_type = models.CharField(max_length=10)
    req_ip = models.CharField(max_length=20)
    timestamp = models.CharField(max_length=25)

    def __unicode__(self):
        return self.req_url
