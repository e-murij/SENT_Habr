from django.test import TestCase
from django.test.client import Client
from authapp.models import User
from django.core.management import call_command


class TestUserManagement(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()

        self.superuser = User.objects.create_superuser('Admin_test', \
                                                       'test_admin@test.local', 'Qwerty1', is_verify=True)

        self.user = User.objects.create_user('user_test1', 'user_test1@test.local', 'Qwerty1', is_verify=True)

        self.user_with__first_name = User.objects.create_user('user_test2', 'user_test2@test.local', 'Qwerty1', \
                                                              first_name='Test2')

    def test_user_login(self):
        # ������� ��� ������
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)

        self.client.login(username='user_test1', password='Qwerty1')

        response = self.client.get('/auth/login/')
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(response.context['user'], self.user)

        # ������� ����� ������
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user'], self.user)

    def test_user_access(self):
        self.client.login(username='user_test1', password='Qwerty1')
        response = self.client.get('/admin/index')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.context['user'], self.user)

    #
    #     # ������� ����������������� ����� � �������
    #     self.client.login(username='Admin_test', password='Qwerty1')
    #     response = self.client.get('/admin/')
    #     self.assertEqual(response.context['user'], self.user)

    # def tearDown(self):
    #     call_command('sqlsequencereset',
    #                  'mainapp',
    #                  'articleapp',
    #                  'persaccapp',
    #                  'authapp',
    #                  'commentapp',
    #                  'likeapp',
    #                  'notificationapp',
    #                  'searchapp',
    #                  )
