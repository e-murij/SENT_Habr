from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from articleapp.models import Article
from authapp.models import User
from persaccapp.services import get_articles_by_author


class PersonalDetailView(DetailView):
    """Отображение личной страницы пользователя"""
    template_name = 'persaccapp/personal_page.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(PersonalDetailView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['title'] = 'Personal Page'
        return context


class MyArticlesList(LoginRequiredMixin, ListView):
    """Отображение списка статей созданных залогиненным пользователем"""
    template_name = 'persaccapp/my_articles.html'
    model = Article

    def get_queryset(self):
        queryset = super(MyArticlesList, self).get_queryset()
        return get_articles_by_author(queryset, self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(MyArticlesList, self).get_context_data(**kwargs)
        context['title'] = 'My Articles'
        return context
