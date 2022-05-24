from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.urls import reverse

from SENT_HABR import settings
from authapp.models import User


def send_verify_mail(user):
    """Отправка верифекационного письма пользователю user"""
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])
    title = f'Подтверждение учетной записи {user.username}'
    message = f'Для подтверждения учетной записи {user.username} на сайте {settings.DOMAIN_NAME} - пройдите по ссылке: ' \
              f'< a href="{settings.DOMAIN_NAME}{verify_link}" > Активировать </a>'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def get_user_by_id(user_id):
    """Получене пользователя с id = user_id"""
    return get_object_or_404(User, pk=user_id)