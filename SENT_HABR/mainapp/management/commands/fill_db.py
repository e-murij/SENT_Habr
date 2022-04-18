import json
import os

from django.core.management import BaseCommand
from mixer.backend.django import mixer

from articleapp.models import Section, Tag, Article
from authapp.models import User

JSON_PATH = 'mainapp/jsons'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='UTF-8') as file:
        return json.load(file)


class Command(BaseCommand):
    def handle(self, *args, **options):

        sections = load_from_json('sections')
        Section.objects.all().delete()
        for section in sections:
            Section(**section).save()
        tags = load_from_json('tags')
        Tag.objects.all().delete()
        for tag in tags:
            Tag(**tag).save()

        User.objects.all().delete()
        users = mixer.cycle(10).blend(User)

        Article.objects.all().delete()

        articles = mixer.cycle(40).blend(Article, section=mixer.SELECT, author=mixer.SELECT, is_published=True)
        User.objects.create_superuser(username='admin', password='admin', first_name='admin')
