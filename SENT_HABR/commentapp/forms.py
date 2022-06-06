from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """Отображение формы комментария"""
    class Meta:
        model = Comment
        fields = ('content',)
