from django import forms

from .models import Article


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    # Всем полям формы добавляется значение 'form-control' http-атрибута 'class'
    def __init__(self, *args, **kwargs):
        super(ArticleCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
