from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView
from authapp.forms import UserRegisterForm, UserAuthenticationForm
from authapp.models import User


class LoginFormView(FormView):
    form_class = UserAuthenticationForm
    template_name = "authapp/login_form.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

    def get_context_data(self):
        context = super(LoginFormView, self).get_context_data()
        title = 'Login'
        context.update({'title': title})
        return context


class RegisterFormView(FormView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('auth:edit')
    template_name = "authapp/register_form.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def get_context_data(self):
        context = super(RegisterFormView, self).get_context_data()
        title = 'Register'
        context.update({'title': title})
        return context


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class Edit(ListView):  # UpdateView
    template_name = 'authapp/edit_form.html'
    model = User
