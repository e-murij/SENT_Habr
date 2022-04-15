import json
import os

from django.core.management import BaseCommand

from articleapp.models import Section
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

        User.objects.create_superuser(username='admin', password='admin', first_name='admin')