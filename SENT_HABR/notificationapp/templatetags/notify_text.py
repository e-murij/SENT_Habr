from django import template
from commentapp.models import Comment
from likeapp.models import LikeDislike

register = template.Library()

@register.filter(name='notify_text')
def notify_text(notify_object):
    content_type = notify_object.content_type.model
    if content_type == 'comment':
        try:
            obj = Comment.objects.get(pk=notify_object.object_id)
            return f' Вашу статью "{obj.article.title}" прокоментировал пользователь {obj.user.username}'
        except LikeDislike.DoesNotExist:
            return f'Комментарий удален'
    if content_type == 'likedislike':
        try:
            obj = LikeDislike.objects.get(pk=notify_object.object_id)
            if obj.content_type.model == 'article':
                return f'Статью "{obj.content_object}" oценил пользователь {obj.user.username}'
            elif obj.content_type.model == 'comment':
                return f'Комментарий к статье "{obj.content_object.article}" oценил пользователь {obj.user.username}'
            elif obj.content_type.model == 'user':
                return f'Вас oценил пользователь {obj.user.username}'
        except LikeDislike.DoesNotExist:
            return f'Лайк/дизлайк удален'


