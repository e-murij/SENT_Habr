from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.forms.widgets import CheckboxSelectMultiple, CheckboxInput

from .models import Article, Tag


class ArticleCreateForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Содержание')

    class Meta:
        model = Article
        exclude = ('author', 'is_active',)

    # Всем полям формы добавляется значение 'form-control' http-атрибута 'class'
    def __init__(self, *args, **kwargs):
        super(ArticleCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields["tags"].widget = CheckboxSelectMultiple()
        self.fields["tags"].queryset = Tag.objects.all()
        self.fields["is_published"].widget = CheckboxInput()
