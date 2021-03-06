from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from likeapp.services import LikeDislikeManager


class LikeDislike(models.Model):
    """Лайк/дизлайк для любого типа объектов приложения"""
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Не нравится'),
        (LIKE, 'Нравится')
    )

    vote = models.SmallIntegerField(
        verbose_name='Голос',
        choices=VOTES,
    )
    user = models.ForeignKey(
        'authapp.User',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Пользователь',
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = LikeDislikeManager()
