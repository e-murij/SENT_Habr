from django.urls import path

from commentapp.views import CommentCreate

app_name = 'commentapp'

urlpatterns = [
    path("<int:pk>/", CommentCreate.as_view(), name="create"),
]
