from django.db import models
from django.contrib.contenttypes.models import ContentType

from authapp.models import TimeStampMixin


class Notification(TimeStampMixin):
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

    class Meta:
        db_table = "notifications"
        ordering = ("-updated_at",)
