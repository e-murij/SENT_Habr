def get_articles_by_author(queryset, author_id):
    """Возвращает все неудаленные статьи, принадлежащие автору с id=author_id, отсортированные по дате изменения"""
    return queryset.filter(is_active=True, author=author_id)