from django.urls import path
from .views import PersonalDetailView

app_name = 'account'

urlpatterns = [
    path('<int:pk>/', PersonalDetailView.as_view(), name='personal_page'),
]
