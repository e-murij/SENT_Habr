from django.urls import path
from .views import PersonalDetailView, MyArticlesList

app_name = 'account'

urlpatterns = [
    path('<int:pk>/', PersonalDetailView.as_view(), name='personal_page'),
    path('my_articles/', MyArticlesList.as_view(), name='my_articles')
]
