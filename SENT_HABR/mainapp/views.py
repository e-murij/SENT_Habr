from django.views.generic import ListView
from articleapp.models import Article


class IndexListView(ListView):
    template_name = 'mainapp/index.html'
    model = Article


class DesignListView(ListView):
    template_name = 'mainapp/design.html'
    model = Article


class WebDevelopmentListView(ListView):
    template_name = 'mainapp/web_development.html'
    model = Article


class MobileDevelopmentListView(ListView):
    template_name = 'mainapp/mobile_development.html'
    model = Article


class MarketingListView(ListView):
    template_name = 'mainapp/marketing.html'
    model = Article


class HelpListView(ListView):
    template_name = 'mainapp/help.html'
    model = Article


class SectionListView(ListView):
    template_name = 'mainapp/index.html'
    model = Article
