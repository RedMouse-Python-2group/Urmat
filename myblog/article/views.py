from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from django.views.generic import ListView

from article.models import Article, Categories

# Create your views here.

class ArticlesList(ListView):
    model = Article, Categories
    template_name="article/articles.html"