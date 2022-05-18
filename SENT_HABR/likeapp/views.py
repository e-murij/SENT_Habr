import json
from django.http import HttpResponse
from django.views import View
from django.contrib.contenttypes.models import ContentType

from likeapp.models import LikeDislike
from likeapp.services import content_owner
from notificationapp.services import create_notify, delete_notif_about_object


class VotesView(View):
    model = None
    vote_type = None

    def post(self, request, pk):
        if request.user.is_authenticated:
            obj = self.model.objects.get(pk=pk)
            content_type_obj = ContentType.objects.get_for_model(obj)
            user = content_owner(obj)
            try:
                likedislike = LikeDislike.objects.get(content_type=content_type_obj,
                                                      object_id=obj.id,
                                                      user=request.user)
                if likedislike.vote is not self.vote_type:
                    likedislike.vote = self.vote_type
                    likedislike.save(update_fields=['vote'])
                    create_notify(user=user, content_type=ContentType.objects.get_for_model(likedislike),
                                  object_id=likedislike.pk)
                    result = True
                else:
                    delete_notif_about_object(content_type=ContentType.objects.get_for_model(likedislike),
                                              object_id=likedislike.pk)
                    likedislike.delete()
                    result = False
            except LikeDislike.DoesNotExist:
                new_obj = obj.votes.create(user=request.user, vote=self.vote_type)
                create_notify(user=user, content_type=ContentType.objects.get_for_model(new_obj),
                              object_id=new_obj.pk)
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
