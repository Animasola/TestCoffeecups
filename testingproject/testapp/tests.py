from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from testingproject.testapp.models import MyInfo


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
