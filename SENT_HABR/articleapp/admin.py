from django.contrib import admin

from articleapp.models import Tag, Section, Article

admin.site.register(Tag)
admin.site.register(Section)
admin.site.register(Article)
