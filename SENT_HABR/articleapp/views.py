from django.views.generic import ListView
from articleapp.models import Article

from .forms import ArticleCreateForm


class ArticleDetailView(ListView):  # DetailView
    template_name = 'articleapp/article_read.html'
    model = Article


class ArticleEditView(ListView):  # UpdateView
    template_name = 'articleapp/article_edit.html'
    model = Article


class ArticleDeleteView(ListView):  # DeleteView
    template_name = 'articleapp/article_delete.html'
    model = Article


class ArticleCreateView(ListView):  # CreateView
    template_name = 'articleapp/article_create.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleCreateView, self).get_context_data(**kwargs)
        context['form_class'] = ArticleCreateForm
        return context
