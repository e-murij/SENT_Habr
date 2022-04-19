def get_all_articles(queryset):
    """Возвращает все неудаленные и опубликованные статьи, отсортированные по дате изменения"""
    return queryset.filter(is_active=True, is_published=True)
