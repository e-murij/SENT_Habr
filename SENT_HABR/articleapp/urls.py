from django.urls import path
from .views import ArticleEditView, ArticleCreateView, ArticleDeleteView, ArticleDetailView

app_name = 'articleapp'

urlpatterns = [
    path('<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', ArticleEditView.as_view(), name='edit'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
]
