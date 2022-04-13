from django.urls import path, include

from .views import IndexListView, HelpListView, SectionListView

urlpatterns = [
    path('', IndexListView.as_view()),
    path('<int:pk>/', SectionListView.as_view(), name='section'),
    path('help', HelpListView.as_view(), name='help'),
    path('auth/', include('authapp.urls', namespace='auth'), name='auth'),
    path('article/', include('articleapp.urls', namespace='article'), name='article'),
    path('account/', include('persaccapp.urls', namespace='account'), name='account'),
]
