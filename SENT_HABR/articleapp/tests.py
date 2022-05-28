from django.test import TestCase
from django.test.client import Client
from django.core.management import call_command
from articleapp.models import Article


# Create your tests here.


class TestArticleappSmoke(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()

    def test_articles_urls(self):
        for article in Article.objects.all():
            response = self.client.get(f'/article/{article.pk}/')
            self.assertEqual(response.status_code, 200)
            print(f'article/{article.pk}, status_code:{response.status_code}')

