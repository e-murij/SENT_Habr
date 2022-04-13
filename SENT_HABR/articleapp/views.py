from django.views.generic import ListView
from articleapp.models import Article


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
