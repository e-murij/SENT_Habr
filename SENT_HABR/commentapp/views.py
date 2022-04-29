from django.shortcuts import render, redirect
from django.views import View

from articleapp.models import Article
from commentapp.forms import CommentForm


class CommentCreate(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        article = Article.objects.get(id=pk)
        user = self.request.user
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.article = article
            form.user = user
            form.save()
        return redirect('article:detail', pk=article.pk)
