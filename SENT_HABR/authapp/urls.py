from django.urls import path

from authapp.views import RegisterFormView, EditUser, EditProfile, LoginFormView, LogoutView

app_name = 'authapp'

urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterFormView.as_view(), name='register'),
    path('edit_user/<int:pk>/', EditUser.as_view(), name='edit_user'),
    path('edit_profile/<int:pk>/', EditProfile.as_view(), name='edit_profile'),
]
