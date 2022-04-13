from django.contrib.auth.models import AbstractUser
from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, TimeStampMixin):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)

    class Meta:
        db_table = "users"


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'
    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'Ж'),
    )
    user = models.OneToOneField(
        User,
        unique=True,
        null=False,
        db_index=True,
        on_delete=models.CASCADE
    )
    birthday = models.DateField(
        verbose_name='дата рождения',
        blank=True,
        default=None,
    )
    about_me = models.TextField(
        verbose_name='о себе',
        max_length=512,
        blank=True
    )
    gender = models.CharField(
        verbose_name='пол',
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True
    )

    class Meta:
        db_table = "user_profiles"
