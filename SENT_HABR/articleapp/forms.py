from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.forms.widgets import CheckboxSelectMultiple, CheckboxInput

from .models import Article, Tag, Section


class ArticleUpdateForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Содержание')
    status = forms.ChoiceField(required=False, widget=forms.RadioSelect,
                               choices=Article.STATUS_CHOICES,
                               label='Отправить на модерацию или сохранить как черновик')

    class Meta:
        model = Article
        exclude = ('author', 'is_active', 'is_published')

    # Всем полям формы добавляется значение 'form-control' http-атрибута 'class'
    def __init__(self, *args, **kwargs):
        super(ArticleUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'status':
                field.widget.attrs['class'] = 'form-control'
        if self.instance.section.slug == 'help':
            self.fields["section"].queryset = Section.objects.filter(slug='help')
        else:
            self.fields["section"].queryset = Section.objects.exclude(slug='help')
        self.fields["tags"].widget = CheckboxSelectMultiple()
        self.fields["tags"].queryset = Tag.objects.all()


class ArticleCreateForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Содержание')
    status = forms.ChoiceField(widget=forms.RadioSelect,
                               choices=Article.STATUS_CHOICES,
                               label='Отправить на модерацию или сохранить как черновик')

    class Meta:
        model = Article
        exclude = ('author', 'is_active', 'is_published')

    # Всем полям формы добавляется значение 'form-control' http-атрибута 'class'
    def __init__(self, *args, **kwargs):
        super(ArticleCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'status':
                field.widget.attrs['class'] = 'form-control'
        self.fields["section"].queryset = Section.objects.exclude(slug='help')
        self.fields["tags"].widget = CheckboxSelectMultiple()
        self.fields["tags"].queryset = Tag.objects.all()
