from django.urls import path

from authapp.views import Login, Register, Logout, Edit

app_name = 'authapp'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('edit/', Edit.as_view(), name='edit'),
]
