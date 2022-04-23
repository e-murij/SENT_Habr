from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView, UpdateView
from authapp.forms import UserRegisterForm, UserAuthenticationForm, UpdateProfileForm, UpdateUserForm
from authapp.models import User, UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginFormView(FormView):
    form_class = UserAuthenticationForm
    template_name = "authapp/login_form.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

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
        return HttpResponseRedirect('/')


class EditProfile(LoginRequiredMixin, UpdateView):
    login_url = 'auth:login'
    form_class = UpdateProfileForm
    template_name = 'authapp/edit_profile.html'
    # success_url = reverse_lazy('auth:edit_profile')
    model = UserProfile

    def form_valid(self, form):
        form.save()
        return super(EditProfile, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EditProfile, self).get_context_data(**kwargs)
        title = 'Edit Profile'
        context.update({'title': title})
        return context

    def get_success_url(self):
        return reverse_lazy('auth:edit_profile', kwargs={'pk': self.kwargs['pk']})

    def dispatch(self, request, *args, **kwargs):
        """
        Проверка пользователя, в случае если пользователь пытается перейти на url
        редактирования другого пользователя - произойдет переход на публичную страничку этого пользователя
        """
        if kwargs['pk'] != request.user.pk:
            return HttpResponseRedirect(reverse('account:personal_page', args=[kwargs["pk"]]))

        return super(EditProfile, self).dispatch(request, *args, **kwargs)


class EditUser(LoginRequiredMixin, UpdateView):
    login_url = 'auth:login'
    form_class = UpdateUserForm
    # success_url = reverse_lazy('auth:edit_user')
    template_name = 'authapp/edit_user.html'
    model = User

    def form_valid(self, form):
        form.save()
        return super(EditUser, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EditUser, self).get_context_data(**kwargs)
        title = 'Edit User'
        context.update({'title': title})
        return context

    def get_success_url(self):
        return reverse_lazy('auth:edit_user', kwargs={'pk': self.kwargs['pk']})

    def dispatch(self, request, *args, **kwargs):
        """
        Проверка пользователя, в случае если пользователь пытается перейти на url
        редактирования другого пользователя - произойдет переход на публичную страничку этого пользователя
        """
        if kwargs['pk'] != request.user.pk:
            return HttpResponseRedirect(reverse('account:personal_page', args=[kwargs["pk"]]))

        return super(EditUser, self).dispatch(request, *args, **kwargs)
