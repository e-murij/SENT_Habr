from django.urls import path

from notificationapp.views import NotificationsList, MarkAsRead

app_name = 'notification'

urlpatterns = [
    path('<int:pk>/', NotificationsList.as_view(), name='my_notifications'),
    path('mark_as_read/<int:pk>/', MarkAsRead.as_view(), name='mark_as_read'),
]
