from django.views import View
from django.views.generic import ListView, TemplateView
from articleapp.models import Article
from articleapp.services import get_articles_by_section, queryset_for_articles, \
    get_all_published_articles


class IndexListView(ListView):
    """Главная страница сайта с выводом списка всех статей, отсортированных по дате изменения """
    template_name = 'mainapp/index.html'
    model = Article
    paginate_by = 5

    def get_queryset(self):
        queryset = queryset_for_articles()
        return get_all_published_articles(queryset)

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['title'] = 'all_articles'
        return context


class SectionListView(ListView):
    """Страницы сайта с выводом списка всех статей, отсортированных по разделам """
    template_name = 'mainapp/index.html'
    model = Article
    paginate_by = 10

    def get_queryset(self):
        queryset = queryset_for_articles()
        return get_articles_by_section(queryset, self.kwargs['section_slug'])

    def get_context_data(self, **kwargs):
        context = super(SectionListView, self).get_context_data(**kwargs)
        context['title'] = self.kwargs['section_slug']
        return context


class HelpView(TemplateView):
    """Вывод страницы помощь с основными правилами и механиками сайта"""
    template_name = 'mainapp/habr_help.html'

    def get_context_data(self, **kwargs):
        context = super(HelpView, self).get_context_data(**kwargs)
        help_article = get_articles_by_section(queryset_for_articles(), 'help').first()
        context['help_article'] = help_article
        return context


