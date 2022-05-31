from django.contrib import admin
from django.urls import reverse

from notificationapp.models import Notification, NotificationCommentModeration


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'read')
    list_display_links = ('id', 'user', 'read')


class NotificationCommentModerationAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'is_check', 'created_at', 'view_moder_link')
    list_display_links = ('id', 'comment', 'is_check', 'created_at')

    def view_moder_link(self, obj):
        from django.utils.html import format_html
        if obj.comment.parent:
            url = (reverse("admin:commentapp_comment_change", args=(obj.comment.parent.pk,)))
            return format_html('<a href="{}"> комментарий </a>', url)
        else:
            url = (reverse("admin:articleapp_article_change", args=(obj.comment.article.pk,)))
            return format_html('<a href="{}"> статья </a>', url)

    view_moder_link.short_description = "объект для модерации"


admin.site.register(Notification, NotificationAdmin)
admin.site.register(NotificationCommentModeration, NotificationCommentModerationAdmin)
