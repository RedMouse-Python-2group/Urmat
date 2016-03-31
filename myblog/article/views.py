from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from django.views.generic import ListView

from article.models import Article, Categories


# Create your views here.

class ArticlesList(ListView):
    model = Article
    template_name="article/articles.html"

    def get_context_data(self, **kwargs):
        context = super(ArticlesList, self).get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
       # context['menu'] = Menu.objects.all()
        return context