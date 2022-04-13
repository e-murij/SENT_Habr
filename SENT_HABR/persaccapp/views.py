from django.views.generic import ListView

from authapp.models import User


class PersonalDetailView(ListView):  # DetailView
    template_name = 'persaccapp/personal_page.html'
    model = User
