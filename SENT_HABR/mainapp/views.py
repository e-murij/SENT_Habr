from django.views.generic import ListView
from articleapp.models import Article
from mainapp.services import get_all_articles, get_articles_by_section


class IndexListView(ListView):
    template_name = 'mainapp/index.html'
    model = Article

    def get_queryset(self):
        queryset = super(IndexListView, self).get_queryset()
        return get_all_articles(queryset)

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['title'] = 'all_articles'
        return context


class SectionListView(ListView):
    template_name = 'mainapp/index.html'
    model = Article

    def get_queryset(self):
        queryset = super(SectionListView, self).get_queryset()
        return get_articles_by_section(queryset, self.kwargs['section_slug'])

    def get_context_data(self, **kwargs):
        context = super(SectionListView, self).get_context_data(**kwargs)
        context['title'] = self.kwargs['section_slug']
        return context
