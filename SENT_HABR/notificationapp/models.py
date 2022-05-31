from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.contrib.contenttypes.models import ContentType

from authapp.models import TimeStampMixin


class Notification(TimeStampMixin):
    """Уведомления для пользователей"""
    user = models.ForeignKey(
        'authapp.User',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Пользователь',
    )
    read = models.BooleanField(
        default=False
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )
    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey()

    class Meta:
        db_table = "notifications"
        ordering = ("-updated_at",)
        verbose_name = "Уведомление для пользователя"
        verbose_name_plural = "Уведомления для пользователей"


class NotificationCommentModeration(TimeStampMixin):
    """Уведомления для модераторов"""
    comment = models.ForeignKey(
        'commentapp.Comment',
        on_delete=models.CASCADE,
        verbose_name='комментарий',
    )
    is_check = models.BooleanField(
        default=False
    )

    class Meta:
        db_table = "notifications_comment_moderation"
        ordering = ("-is_check", "-created_at")
        verbose_name = "Уведомление для модератора"
        verbose_name_plural = "Уведомления для модератора"
