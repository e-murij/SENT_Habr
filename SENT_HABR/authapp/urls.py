from django.urls import path
from django.views.generic import TemplateView

from authapp.views import RegisterFormView, LoginFormView, LogoutView, EditView, VerifyView, VerifyEmailView,\
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
]
