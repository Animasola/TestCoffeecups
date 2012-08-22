from django.test import TestCase
from django.test.client import Client
from django.template import Template
from django.template import Context
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from StringIO import StringIO
import sys
from django_any import any_model
from django.db.models import get_models
from datetime import datetime
from PIL import Image

from testingproject.testapp.models import MyInfo, ReqsHistory, ModelLog
from testingproject.testapp.forms import MyInfoForm


def create_myinfo_exemplar():
    obj = MyInfo.objects.create(name="Petro",
                                surname="Petrenko",
                                birth_date="1986-10-10",
                                bio="Theres nothing to tell",
                                email="petro@gmail.com",
                                jabber="petro@akhavr.com",
                                skype="petro1986",
                                other_cont="petro@mail.ru")
    obj.save()


class MainPageTest(TestCase):

    def setUp(self):
        self.model_obj = MyInfo.objects.create(name="Petro",
            surname="Petrenko",
            birth_date="1986-10-10",
            bio="Theres nothing to tell",
            email="petro@gmail.com",
            jabber="petro@akhavr.com",
            skype="petro1986",
            other_cont="petro@mail.ru")
        self.model_obj.save()
        self.petya = MyInfo.objects.get(name='Petro')
        self.client = Client()

    def tearDown(self):
        self.model_obj = None
        self.petya = None
        self.client = None

    def test_obj_as_string(self):
        self.assertEqual(str(self.petya), 'Petro Petrenko')

    def test_model_fields(self):
        self.assertEqual(self.model_obj.name, 'Petro')
        self.assertEqual(self.model_obj.surname, 'Petrenko')
        self.assertEqual(self.model_obj.bio, 'Theres nothing to tell')
        self.assertEqual(self.model_obj.email, 'petro@gmail.com')
        self.assertEqual(self.model_obj.jabber, 'petro@akhavr.com')
        self.assertEqual(self.model_obj.skype, 'petro1986')
        self.assertEqual(self.model_obj.other_cont, 'petro@mail.ru')

    def test_object_delete(self):
        self.petya.delete()
        self.assertNotEqual(MyInfo.objects.filter(name="Petro"),
            'Petro')

    def test_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main_page.html')

    def test_page_contens(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Assignment', status_code=200)
        self.assertContains(response, self.petya.name, status_code=200)
        self.assertContains(response, self.petya.surname, status_code=200)
        self.assertContains(response, self.petya.bio, status_code=200)
        self.assertContains(response, self.petya.email, status_code=200)
        self.assertContains(response, self.petya.jabber, status_code=200)
        self.assertContains(response, self.petya.skype, status_code=200)
        self.assertContains(response, self.petya.other_cont, status_code=200)

    def test_template_context(self):
        response = self.client.get(reverse('home'))
        self.assertTrue('myinfo' in response.context)
        self.assertTrue('Petro' in str(response.context['myinfo']))


class RequestsLogTemplateTest(TestCase):
    """Tests for middleware (ticket_3)"""

    def setUp(self):
        self.client = Client()

    def tearDown(self):
        self.client = None

    def test_template(self):
        response = self.client.get(reverse('reqslog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reqs_log.html')

    def test_reqlog_page(self):
        response = self.client.get(reverse('reqslog'))
        self.assertContains(response, 'from', count=1, status_code=200)
        for n in xrange(15):
            response = self.client.get(reverse('reqslog'))
        self.assertContains(response, 'request to', count=10, status_code=200)
        self.assertEqual(ReqsHistory.objects.filter().count(),
                    16)

    def test_templ_context(self):
        response = self.client.get(reverse('reqslog'))
        self.assertTrue('requests' in response.context)
        log = ReqsHistory.objects.get(pk=1)
        self.assertContains(response, log.req_url, status_code=200)
        self.assertContains(response, log.req_type, status_code=200)
        self.assertContains(response, log.req_ip, status_code=200)


class RequestLogModelTest(TestCase):

    def setUp(self):
        self.new_url = ReqsHistory(
            timestamp='2012-04-20',
            req_url='google',
            req_type="POST",
            req_ip="10.10.157.17",
            )

    def tearDown(self):
        self.new_url = None

    def test_object_as_string(self):
        self.new_url.save()
        self.assertEqual(str(self.new_url), 'google')

    def test_save_object(self):
        self.new_url.save()
        obj = ReqsHistory.objects.get(req_url="google")
        self.assertEqual(obj.req_url, 'google')
        self.assertEqual(obj.req_type, 'POST')
        self.assertTrue(obj.timestamp)

    def test_delete_object(self):
        self.new_url.save()
        ReqsHistory.objects.filter(req_url="google")
        self.assertNotEqual(ReqsHistory.objects.filter(req_url="google"),
                     'google')


class TemplateContextProcTest(TestCase):

    def setUp(self):
        self.client = Client()

    def tearDown(self):
        self.client = None

    def test_context(self):
        user = self.client.login(username='animasola', password='hal498p')
        response = self.client.get(reverse('home'))
        self.assertTrue('django_settings' in response.context)


class FormValidationTest(TestCase):

    def setUp(self):
        self.file_obj = StringIO()
        self.image = Image.new("RGBA", size=(50, 50), color=(256, 0, 0))
        self.post_dict = {'name': "Petro",
                'surname': "Petrenko",
                'birth_date': '1986-12-20',
                'bio': 'Theres nothing to tell',
                'email': 'petro@mail.ru',
                'jabber': 'annima@akhavr.com',
                'skype': 'petro1986',
                'other_cont': 'petro@ukr.net'}

    def tearDown(self):
        self.file_obj = None
        self.image = None
        self.post_dict = None

    def test_forma(self):
        self.image.save(self.file_obj, 'png')
        self.file_obj.name = 'test_%s.png' % datetime.now().microsecond
        self.file_obj.seek(0)
        file_dict = {
             'my_photo': SimpleUploadedFile(self.file_obj.name,
                                                self.file_obj.read())}
        form = MyInfoForm(self.post_dict, file_dict)
        self.assertTrue(form.is_valid())
        form.save()
        user = self.client.login(username='animasola', password='hal498p')
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Assignment', status_code=200)
        self.assertContains(response, self.post_dict['name'], status_code=200)
        self.assertContains(response, self.post_dict['surname'],
                    status_code=200)
        self.assertContains(response, self.post_dict['bio'], status_code=200)
        self.assertContains(response, self.post_dict['email'],
                    status_code=200)
        self.assertContains(response, self.post_dict['jabber'],
                    status_code=200)
        self.assertContains(response, self.post_dict['skype'], status_code=200)
        self.assertContains(response, self.post_dict['other_cont'],
                    status_code=200)
        self.assertContains(response, self.file_obj.name, status_code=200)


class TemplateTagTest(TestCase):

    def setUp(self):
        create_myinfo_exemplar()
        self.petya = MyInfo.objects.get(name='Petro')
        self.client = Client()

    def test_tag(self):
        t = Template('{% load admin_edit_tag %}{% admin_url obj %}')
        c = Context({"obj": self.petya})
        url = u'/admin/testapp/myinfo/2/'
        self.failUnlessEqual(url, t.render(c))
        response = self.client.get(t.render(c))
        self.assertEqual(response.status_code, 200)


class DjangoCommandsTesting(TestCase):

    def setUp(self):
        self.errpart = StringIO()
        self.outpart = StringIO()

    def test_command(self):
        call_command("models_stat", stderr=self.errpart, stdout=self.outpart)
        self.errpart.seek(0)
        self.outpart.seek(0)
        error_list = self.errpart.readlines()
        out_list = self.outpart.readlines()
        for model in get_models():
            self.assertTrue("error: [%s] - %s objects\n" % (model.__name__,
                        model._default_manager.count()) in error_list or \
                        "error: [%s] - %s objects" % (model.__name__,
                        model._default_manager.count()) in error_list)
            self.assertTrue("[%s] - %s objects\n" % (model.__name__,
                        model._default_manager.count()) in out_list or \
                        "[%s] - %s objects" % (model.__name__,
                        model._default_manager.count()) in out_list)
        self.assertEqual(len(get_models()), len(error_list))
        self.assertEqual(len(get_models()), len(out_list))

    def tearDown(self):
        self.errpart = None
        self.outpart = None


class TestingSignals(TestCase):
    def setUp(self):
        self.modlog = ModelLog.objects.filter().delete()
        self.my_info = any_model(MyInfo, my_photo='')

    def test_creation(self):
        log_created = ModelLog.objects.get(pk=1)
        self.assertEquals(log_created.model, "MyInfo")
        self.assertEquals(log_created.action, "Created")
        self.assertEquals(log_created.target_instance,
                          "%s %s" % (self.my_info.name, self.my_info.surname))

    def test_alteration_deletion(self):
        me = MyInfo.objects.get(pk=1)
        me.name = "Andy"
        me.save()
        log_altered = ModelLog.objects.get(pk=2)
        self.assertEquals(log_altered.model, "MyInfo")
        self.assertEquals(log_altered.action, "Altered")
        self.assertEquals(log_altered.target_instance,
                          "%s %s" % (me.name, me.surname))
        me.delete()
        log_deleted = ModelLog.objects.get(pk=3)
        self.assertEquals(log_deleted.model, "MyInfo")
        self.assertEquals(log_deleted.action, "Deleted")
        self.assertEquals(log_deleted.target_instance,
                          "%s %s" % (me.name, me.surname))
        self.assertTrue(ModelLog.objects.filter().count() == 3)
