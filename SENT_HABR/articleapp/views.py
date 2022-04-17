from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView
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


class ArticleCreateView(CreateView):
    template_name = 'articleapp/article_create.html'
    form_class = ArticleCreateForm
    success_url = '/'   # todo Change to redirect

    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(ArticleCreateView, self).get_context_data(**kwargs)
        context['form_class'] = ArticleCreateForm
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('auth:login')
        return super(ArticleCreateView, self).dispatch(request, *args, **kwargs)
