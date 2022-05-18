from django.urls import path, include

from .views import IndexListView, SectionListView

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('<slug:section_slug>/', SectionListView.as_view(), name='section'),
    path('auth/', include('authapp.urls', namespace='auth'), name='auth'),
    path('article/', include('articleapp.urls', namespace='article'), name='article'),
    path('account/', include('persaccapp.urls', namespace='account'), name='account'),
    path('comment/', include('commentapp.urls', namespace='comment'), name='comment'),
    path('likes/', include('likeapp.urls', namespace='likes'), name='likes'),
    path('notification/', include('notificationapp.urls', namespace='notification'), name='notification'),
]
