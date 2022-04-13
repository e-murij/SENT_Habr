from django.db import models

from authapp.models import TimeStampMixin, User


class Tag(TimeStampMixin):
    name = models.CharField(
        verbose_name='тэг',
        max_length=128,
    )

    class Meta:
        db_table = "tags"


class Section(TimeStampMixin):
    name = models.CharField(
        verbose_name='тэг',
        max_length=128,
    )

    class Meta:
        db_table = "sections"


class Article(TimeStampMixin):
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='автор',
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='тэги',
        null=True,
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        verbose_name='раздел',
    )
    content = models.TextField(
        verbose_name='содержание',
        blank=True,
    )
    is_active = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        db_table = "articles"
