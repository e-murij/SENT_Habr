from django.db import models

from articleapp.models import Article
from authapp.models import User, TimeStampMixin


class Comment(TimeStampMixin):
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
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    article = models.ForeignKey(
        Article,
        verbose_name='Статья',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.user.username} - {self.article}'

    class Meta:
        db_table = "comments"
        ordering = ("-updated_at",)
