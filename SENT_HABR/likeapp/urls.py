from django.urls import path
from articleapp.models import Article
from authapp.models import User
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
    path('user/<int:pk>/like/', VotesView.as_view(model=User, vote_type=LikeDislike.LIKE), name='user_like'),
    path('user/<int:pk>/dislike/', VotesView.as_view(model=User, vote_type=LikeDislike.DISLIKE),
         name='user_dislike'),
]
