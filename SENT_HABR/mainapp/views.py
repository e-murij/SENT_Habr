from django.views.generic import ListView
from articleapp.models import Article


class IndexListView(ListView):
    template_name = 'mainapp/index.html'
    model = Article


class HelpListView(ListView):
    template_name = 'mainapp/help.html'
    model = Article


class SectionListView(ListView):
    template_name = 'mainapp/index.html'
    model = Article
