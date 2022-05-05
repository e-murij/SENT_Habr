import json
from django.http import HttpResponse
from django.views import View
from django.contrib.contenttypes.models import ContentType

from likeapp.models import LikeDislike


class VotesView(View):
    model = None
    vote_type = None

    def post(self, request, pk):
        if request.user.is_authenticated:
            obj = self.model.objects.get(pk=pk)
            try:
                likedislike = LikeDislike.objects.get(content_type=ContentType.objects.get_for_model(obj),
                                                      object_id=obj.id,
                                                      user=request.user)
                if likedislike.vote is not self.vote_type:
                    likedislike.vote = self.vote_type
                    likedislike.save(update_fields=['vote'])
                    result = True
                else:
                    likedislike.delete()
                    result = False
            except LikeDislike.DoesNotExist:
                obj.votes.create(user=request.user, vote=self.vote_type)
                result = True
            return HttpResponse(
                json.dumps({
                    "result": result,
                    "like_count": obj.votes.likes().count(),
                    "dislike_count": obj.votes.dislikes().count(),
                    "sum_rating": obj.votes.sum_rating()
                }),
                content_type="application/json"
            )
        return HttpResponse(
            json.dumps({
                "redirect": "/auth/login",
            }),
            content_type="application/json"
        )
