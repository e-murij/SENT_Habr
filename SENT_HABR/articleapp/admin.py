from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django import forms
from articleapp.models import Tag, Section, Article


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Содержание')
    status = forms.ChoiceField(widget=forms.RadioSelect,
                               choices=Article.STATUS_CHOICES,
                               label='Отправить на модерацию или сохранить как черновик')

    class Meta:
        model = Article
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ArticleAdminForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'status':
                field.widget.attrs['class'] = 'form-control'
        self.fields["tags"].widget = CheckboxSelectMultiple()
        self.fields["tags"].queryset = Tag.objects.all()


class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'is_active', 'is_published', 'status')
    list_display_links = ('id', 'title', 'author', 'is_active', 'is_published', 'status')
    form = ArticleAdminForm
    ordering = ('is_published', '-status')


admin.site.register(Tag, TagAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Article, ArticleAdmin)
