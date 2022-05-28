from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import FormView, TemplateView

from authapp.forms import UserRegisterForm, UserAuthenticationForm, UpdateProfileForm, UpdateUserForm
from authapp.models import User
from authapp.servises import get_user_by_id, send_verify_mail, create_activation_key


class LoginFormView(FormView):
    form_class = UserAuthenticationForm
    template_name = "authapp/login_form.html"

    def form_valid(self, form):
        self.user = form.get_user()
        if self.user.is_verify:
            auth.login(self.request, self.user, backend='django.contrib.auth.backends.ModelBackend')
            next_page = self.request.POST.get('next')
            return HttpResponseRedirect('/') if not next_page or (
                    '/auth/' in next_page) else HttpResponseRedirect(self.request.POST.get('next'))
        return HttpResponseRedirect(reverse_lazy('auth:verify_email', kwargs={'pk': self.user.pk}))

    def get_context_data(self, **kwargs):
        context = super(LoginFormView, self).get_context_data(**kwargs)
        title = 'Login'
        context.update({'title': title})
        return context


class RegisterFormView(FormView):
    form_class = UserRegisterForm
    template_name = "authapp/register_form.html"

    def form_valid(self, form):
        self.user = form.save()
        send_verify_mail(self.user)
        return super(RegisterFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('auth:verify_email', kwargs={'pk': self.user.pk})

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


class VerifyView(View):
    def get(self, request, email, activation_key):
        try:
            user = User.objects.get(email=email)
            if user.activation_key == activation_key:
                user.is_verify = True
                user.save()
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return render(request, 'authapp/verify.html')
            else:
                print(f'activation key error in user: {user.username}')
                return render(request, 'authapp/verify.html')
        except Exception as err:
            print(f'Error activation user: {err.args}')
            return HttpResponseRedirect(reverse('index'))


class VerifyEmailView(TemplateView):
    template_name = 'authapp/verify_email.html'

    def get_context_data(self, **kwargs):
        context = super(VerifyEmailView, self).get_context_data(**kwargs)
        user = get_user_by_id(kwargs['pk'])
        context['unverified_user'] = user
        return context


class RepeatVerifyEmailView(View):
    def get(self, request, *args, **kwargs):
        user = get_user_by_id(kwargs['pk'])
        user.activation_key = create_activation_key(user)
        user.save()
        send_verify_mail(user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
