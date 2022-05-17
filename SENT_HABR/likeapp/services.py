from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Sum


class LikeDislikeManager(models.Manager):
    use_for_related_fields = True

    def likes(self):
        # Забираем queryset с записями больше 0
        return self.get_queryset().filter(vote__gt=0)

    def dislikes(self):
        # Забираем queryset с записями меньше 0
        return self.get_queryset().filter(vote__lt=0)

    def sum_rating(self):
        # Забираем суммарный рейтинг
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0


def content_owner(content_obj):
    obj_type = ContentType.objects.get_for_model(content_obj).model
    if obj_type == 'comment':
        return content_obj.user
    elif obj_type == 'article':
        return content_obj.author
    elif obj_type == 'user':
        return content_obj
