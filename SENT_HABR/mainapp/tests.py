from django.test import TestCase
from django.test.client import Client
from django.core.management import call_command
from articleapp.models import Section


# Create your tests here.


class TestMainappSmoke(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()

    def test_mainapp_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/auth/')
        self.assertEqual(response.status_code, 200)
        # print(response.status_code)
        response = self.client.get('/article/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/account/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/comment/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/likes/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/notification/')
        self.assertEqual(response.status_code, 200)

        for section in Section.objects.all():
            response = self.client.get(f'/{section.slug}/')
            self.assertEqual(response.status_code, 200)


    def tearDown(self):
        call_command('sqlsequencereset', 'mainapp', 'authapp', \
                     'articleapp', 'likeapp', 'commentapp', 'notificationapp', 'persaccapp')


