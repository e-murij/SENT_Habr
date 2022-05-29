from django.db.models import Q

from articleapp.models import Article
from authapp.models import User
from commentapp.models import Comment


def users_search(query):
    """Возвращает пользователей в username или first_name или last_name которых содержится строка query"""
    or_lookup = (Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query))
    users = User.objects.filter(or_lookup)
    return users


def articles_search(query):
    """Возвращает статьи в названии или тексте которых содержится строка query"""
    or_lookup = (Q(title__icontains=query) | Q(content__icontains=query))
    articles = Article.objects.filter(or_lookup)
    return articles


def comments_search(query):
    """Возвращает комментарии в тексте которых содержится строка query"""
    comments = Comment.objects.filter(content__icontains=query)
    return comments
