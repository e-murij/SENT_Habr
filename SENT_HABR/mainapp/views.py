from django.views.generic import ListView
from articleapp.models import Article


class IndexListView(ListView):
    template_name = 'mainapp/index.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class SectionListView(ListView):
    template_name = 'mainapp/index.html'
    model = Article
