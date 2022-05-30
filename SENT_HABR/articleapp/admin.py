from django.contrib import admin
from articleapp.forms import ArticleCreateForm
from articleapp.models import Tag, Section, Article


class ArticleAdminForm(ArticleCreateForm):
    class Meta:
        model = Article
        fields = '__all__'


class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'is_active', 'is_published')
    list_display_links = ('id', 'title', 'author', 'is_active', 'is_published')
    form = ArticleAdminForm


admin.site.register(Tag, TagAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Article, ArticleAdmin)
