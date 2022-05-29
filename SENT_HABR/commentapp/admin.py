from django.contrib import admin

from commentapp.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'parent', 'article')
    list_display_links = ('id', 'user', 'content', 'parent', 'article')


admin.site.register(Comment, CommentAdmin)
