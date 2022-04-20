from django.db import models

from authapp.models import TimeStampMixin, User


class Tag(TimeStampMixin):
    name = models.CharField(
        verbose_name='tag',
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


class Section(TimeStampMixin):
    name = models.CharField(
        verbose_name='section',
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


class Article(TimeStampMixin):
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='author',
    )
    title = models.CharField(
        verbose_name='title',
        max_length=128,
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='tags',
        null=True,
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        verbose_name='section',
    )
    content = models.TextField(
        verbose_name='content',
        blank=True,
    )
    is_active = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "articles"
        ordering = ("-updated_at",)
