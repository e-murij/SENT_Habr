from django.views.generic import ListView

from authapp.models import User


class Login(ListView):  # FormView
    template_name = 'authapp/login_form.html'
    model = User


class Register(ListView):  # CreateView
    template_name = 'authapp/register_form.html'
    model = User


class Logout(ListView):
    template_name = 'authapp/login_form.html'
    model = User


class Edit(ListView):  # UpdateView
    template_name = 'authapp/edit_form.html'
    model = User
