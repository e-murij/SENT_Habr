from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from authapp.models import TimeStampMixin, User
from likeapp.models import LikeDislike


class Tag(TimeStampMixin):
    name = models.CharField(
        verbose_name='тэг',
        max_length=128,
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="URL",
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tags"
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"


class Section(TimeStampMixin):
    name = models.CharField(
        verbose_name='раздел',
        max_length=128,
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="URL",
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "sections"
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"


class Article(TimeStampMixin):
    MODERATION = 'MOD'
    DRAFT = 'DRAFT'
    STATUS_CHOICES = (
        (MODERATION, 'модерация'),
        (DRAFT, 'черновик'),
    )
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='автор',
    )
    title = models.CharField(
        verbose_name='название',
        max_length=128,
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='тэги',
        null=True,
        blank=True,
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
    is_active = models.BooleanField(
        default=True
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='опубликовать'
    )
    status = models.CharField(
        verbose_name='статус статьи',
        max_length=5,
        choices=STATUS_CHOICES,
        default='DRAFT'
    )
    votes = GenericRelation(
        LikeDislike,
        related_query_name='articles',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        db_table = "articles"
        ordering = ("-updated_at",)
