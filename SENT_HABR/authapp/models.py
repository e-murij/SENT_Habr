from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from likeapp.models import LikeDislike


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, TimeStampMixin):
    avatar = models.ImageField(
        upload_to='users_avatars',
        blank=True,
    )
    votes = GenericRelation(
        LikeDislike,
        related_query_name='users',
    )

    def __str__(self):
        return self.username

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
        verbose_name='Дата рождения',
        blank=True,
        null=True,
    )
    about_me = models.TextField(
        verbose_name='Обо мне',
        max_length=512,
        blank=True
    )
    gender = models.CharField(
        verbose_name='Пол',
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True
    )

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

    class Meta:
        db_table = "user_profiles"
