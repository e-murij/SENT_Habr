from django.views.generic import DetailView
from authapp.models import User


class PersonalDetailView(DetailView):
    template_name = 'persaccapp/personal_page.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(PersonalDetailView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
