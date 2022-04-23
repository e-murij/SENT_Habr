from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from authapp.forms import UserRegisterForm, UserAuthenticationForm, UpdateProfileForm, UpdateUserForm


class LoginFormView(FormView):
    form_class = UserAuthenticationForm
    template_name = "authapp/login_form.html"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('account:personal_page', kwargs={'pk': self.request.user.pk})

    def get_context_data(self, **kwargs):
        context = super(LoginFormView, self).get_context_data(**kwargs)
        title = 'Login'
        context.update({'title': title})
        return context


class RegisterFormView(FormView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('auth:login')
    template_name = "authapp/register_form.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RegisterFormView, self).get_context_data(**kwargs)
        title = 'Register'
        context.update({'title': title})
        return context


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class EditView(LoginRequiredMixin, FormView):
    user_form = UpdateUserForm
    profile_form = UpdateProfileForm
    template_name = 'authapp/edit_form.html'

    def get(self, request, *args, **kwargs):
        context = {'user_form': self.user_form(instance=self.request.user),
                   'profile_form': self.profile_form(instance=self.request.user.userprofile),
                   'title': 'Edit User'
                   }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user_form = UpdateUserForm(self.request.POST, self.request.FILES, instance=self.request.user)
        profile_form = UpdateProfileForm(self.request.POST, instance=self.request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('account:personal_page', kwargs={'pk': self.request.user.pk})
