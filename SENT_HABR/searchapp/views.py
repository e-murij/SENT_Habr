from django.shortcuts import render
from django.views import View

from searchapp.servises import articles_search, users_search, comments_search


class SearchView(View):
    """ Отображение разультатов поиска """
    template_name = 'searchapp/search.html'

    def get(self, request):
        context = {'title': 'search'}
        q = request.GET.get('q')
        if q:
            print(q)
            context['articles'] = articles_search(query=q)
            context['users'] = users_search(query=q)
            context['comments'] = comments_search(query=q)
            context['query'] = q

        return render(request=request, template_name=self.template_name, context=context)
