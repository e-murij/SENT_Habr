from articleapp.models import Section, Article
from articleapp.services import get_all_published_articles, queryset_for_articles
from authapp.models import User
from likeapp.services import get_popular_elements


def sections(request):
    """Передача разделов сайта в контекст"""
    sections_menu = Section.objects.all()
    return {
        'sections_menu': sections_menu,
    }


def popular_articles_and_users(request):
    """Передача наиболее популярных пользователей и статей  в контекст"""
    popular_articles = get_popular_elements(get_all_published_articles(queryset_for_articles()), 5)
    popular_users = get_popular_elements(User.objects.all().filter(is_active=True), 5)
    return {
        'popular_articles': popular_articles,
        'popular_users': popular_users,
    }
