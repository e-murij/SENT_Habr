from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView

from authapp.forms import UserRegisterForm
from authapp.models import User


class Login(ListView):  # FormView
    template_name = 'authapp/login_form.html'
    model = User


class RegisterFormView(FormView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('auth:edit')
    template_name = "authapp/register_form.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class Logout(ListView):
    template_name = 'authapp/login_form.html'
    model = User


class Edit(ListView):  # UpdateView
    template_name = 'authapp/edit_form.html'
    model = User
