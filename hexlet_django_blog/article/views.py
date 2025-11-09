from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from hexlet_django_blog.article.models import Article
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        if 'id' in kwargs:
            article = get_object_or_404(Article, pk=kwargs['id'])
            return render(
                request,
                "articles/article.html",
                context={"article": article}
            )
        else:
            articles = Article.objects.all()[:15]
            return render(
                request,
                "articles/index.html",
                context={"articles": articles}
            )