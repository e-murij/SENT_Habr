from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from authapp.views import RegisterFormView, LoginFormView, LogoutView, EditView, VerifyView, VerifyEmailView, \
    RepeatVerifyEmailView

app_name = 'authapp'

urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterFormView.as_view(), name='register'),
    path('edit/', EditView.as_view(), name='edit'),
    path('verify_email/<int:pk>', VerifyEmailView.as_view(), name='verify_email'),
    path('repeat_verify_email/<int:pk>', RepeatVerifyEmailView.as_view(), name='repeat_verify_email'),
    path('verify/<str:email>/<str:activation_key>/', VerifyView.as_view(), name='verify'),
    path('password-reset', auth_views.PasswordResetView.as_view(template_name='authapp/password_reset_form.html',
                                                                email_template_name='authapp/password_reset_email.html',
                                                                success_url=reverse_lazy('auth:password_reset_done')),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="authapp/password_reset_done.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="authapp/password_reset_confirm.html",
                                                     success_url=reverse_lazy("auth:password_reset_complete")),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="authapp/password_reset_complete.html"),
         name='password_reset_complete'),
]
