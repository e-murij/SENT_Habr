from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from articleapp.models import Article
from authapp.models import User, TimeStampMixin
from likeapp.models import LikeDislike
from notificationapp.models import Notification


class Comment(TimeStampMixin):
    """Комментарии к статьям и комментариям(единичная вложенность)"""
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Пользователь',
    )
    content = models.TextField(
        verbose_name='Комментарий',
        max_length=5000,
    )
    parent = models.ForeignKey(
        'self',
        verbose_name='Родитель',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    article = models.ForeignKey(
        Article,
        verbose_name='Статья',
        on_delete=models.CASCADE,
    )
    votes = GenericRelation(
        LikeDislike,
        related_query_name='comments',
    )
    comments = GenericRelation(
        Notification,
        related_query_name='comments',
    )

    def __str__(self):
        return f'{self.content}'

    class Meta:
        db_table = "comments"
        ordering = ("-updated_at",)
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
