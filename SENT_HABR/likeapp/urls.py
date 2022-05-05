from django.urls import path
from articleapp.models import Article
from commentapp.models import Comment
from .models import LikeDislike
from .views import VotesView

app_name = 'likes'

urlpatterns = [
    path('article/<int:pk>/like/', VotesView.as_view(model=Article, vote_type=LikeDislike.LIKE), name='article_like'),
    path('article/<int:pk>/dislike/', VotesView.as_view(model=Article, vote_type=LikeDislike.DISLIKE),
         name='article_dislike'),
    path('comment/<int:pk>/like/', VotesView.as_view(model=Comment, vote_type=LikeDislike.LIKE), name='comment_like'),
    path('comment/<int:pk>/dislike/', VotesView.as_view(model=Comment, vote_type=LikeDislike.DISLIKE),
         name='comment_dislike'),
]
