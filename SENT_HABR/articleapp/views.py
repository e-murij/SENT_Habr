from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from articleapp.models import Article
from articleapp.services import get_comments, get_article_by_id, queryset_for_articles

from .forms import ArticleCreateForm, ArticleUpdateForm


class ArticleDetailView(DetailView):
    """ Просмотр полной статьи с комментариями к ней """
    template_name = 'articleapp/article_read.html'
    model = Article
    queryset = queryset_for_articles()

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Detail article'
        context['article_pk'] = self.kwargs.get('pk')
        context['comments'] = get_comments(self.get_object())
        return context


class ArticleEditView(LoginRequiredMixin, UpdateView):
    """ Изменение статьи автором или администратором сайта"""
    model = Article
    template_name = 'articleapp/article_edit.html'
    form_class = ArticleUpdateForm
    success_url = reverse_lazy('account:my_articles')

    def check_author(self):
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        self.object = form.save()
        if self.object.status == 'DRAFT':
            self.object.is_published = False
            self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(ArticleEditView, self).get_context_data(**kwargs)
        article = get_article_by_id(self.kwargs.get('pk'))
        context['form_class'] = ArticleUpdateForm(instance=article)
        context['title'] = 'edit article'
        return context

    def dispatch(self, request, *args, **kwargs):
        if not self.check_author():
            return redirect('/')
        return super(ArticleEditView, self).dispatch(request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    """ Удаление статьи. Флаги is_actve is_published ставятся в false, фактически статья из базы данных не удаляется"""
    template_name = 'articleapp/article_delete.html'
    success_url = reverse_lazy('account:my_articles')
    model = Article
    queryset = queryset_for_articles()

    def check_author(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.check_author():
            return redirect('/')
        return super(ArticleDeleteView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.is_published = False
        self.object.save()
        return HttpResponseRedirect(self.success_url)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    """ Создание новой статьи """
    template_name = 'articleapp/article_create.html'
    form_class = ArticleCreateForm
    success_url = reverse_lazy('account:my_articles')

    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(ArticleCreateView, self).get_context_data(**kwargs)
        context['form_class'] = ArticleCreateForm
        context['title'] = 'create article '
        return context
