from django.views.generic import ListView
from articleapp.models import Article


class IndexListView(ListView):
    template_name = 'mainapp/index.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class DesignListView(ListView):
    template_name = 'mainapp/design.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super(DesignListView, self).get_context_data(**kwargs)
        context['title'] = 'Design'
        return context


class WebDevelopmentListView(ListView):
    template_name = 'mainapp/web_development.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super(WebDevelopmentListView, self).get_context_data(**kwargs)
        context['title'] = 'Web Development'
        return context


class MobileDevelopmentListView(ListView):
    template_name = 'mainapp/mobile_development.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super(MobileDevelopmentListView, self).get_context_data(**kwargs)
        context['title'] = 'Mobile Development'
        return context


class MarketingListView(ListView):
    template_name = 'mainapp/marketing.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super(MarketingListView, self).get_context_data(**kwargs)
        context['title'] = 'Marketing'
        return context


class HelpListView(ListView):
    template_name = 'mainapp/help.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super(HelpListView, self).get_context_data(**kwargs)
        context['title'] = 'Help'
        return context


class SectionListView(ListView):
    template_name = 'mainapp/index.html'
    model = Article
