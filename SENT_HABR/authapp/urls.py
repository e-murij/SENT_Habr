from django.urls import path

from authapp.views import RegisterFormView, Edit, LoginFormView, LogoutView

app_name = 'authapp'

urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterFormView.as_view(), name='register'),
    path('edit/', Edit.as_view(), name='edit'),
]
