from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from django.views import View

from articleapp.services import get_article_by_id
from commentapp.forms import CommentForm
from notificationapp.models import NotificationCommentModeration
from notificationapp.services import create_notify


class CommentCreate(LoginRequiredMixin, View):
    """ Создание комментария """
    def post(self, request, pk):
        form = CommentForm(request.POST)
        article = get_article_by_id(pk)
        user = self.request.user
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.article = article
            form.user = user
            form.save()
            if '@moderator' in form.content:
                notify_for_moderator = NotificationCommentModeration(comment=form)
                notify_for_moderator.save()
            create_notify(user=article.author, content_type=ContentType.objects.get_for_model(form), object_id=form.pk)
        return redirect('article:detail', pk=article.pk)
