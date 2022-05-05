from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='user_avatar')
def media_folder_users(string):
    if not string:
        # string = 'users_avatars/default.jpg'
        return f'{settings.STATIC_URL}mainapp/images/default_django-icon.png'
    return f'{settings.MEDIA_URL}{string}'

