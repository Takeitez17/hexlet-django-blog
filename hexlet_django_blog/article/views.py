from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    articles = ['Статья о животных', 'Статья и грибах']
    return render( request,
                  'articles/index.html', 
                  context={'articles':articles})
