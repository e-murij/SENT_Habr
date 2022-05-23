from django.shortcuts import get_object_or_404
from articleapp.models import Article


def get_article_by_id(article_id):
    """Возвращает статью с id = article_id """
    article = get_object_or_404(Article, pk=article_id)
    return article


def get_all_articles(queryset):
    """Возвращает все неудаленные и опубликованные статьи, отсортированные по дате изменения"""
    return queryset.filter(is_active=True, is_published=True)


def get_articles_by_section(queryset, section_slug):
    """Возвращает все неудаленные и опубликованные статьи из раздела section_slug, отсортированные по дате изменения"""
    return queryset.filter(is_active=True, is_published=True, section__slug=section_slug)


def get_comments(article):
    """Возвращает все комментарии к статье article"""
    return article.comment_set.filter(parent__isnull=True)

