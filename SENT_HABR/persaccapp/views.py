from django.views.generic import DetailView

from authapp.models import User


class PersonalDetailView(DetailView):
    template_name = 'persaccapp/personal_page.html'
    model = User

