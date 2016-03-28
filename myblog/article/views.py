from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from article import models

# Create your views here.
def index_page(request):
    return "Hello world !"

def articles(request):
    o = Article.objects.all()
    return render(request, 'article/template/articles.html', {'articles': o})

#def article(request, article_id=1):
 #   return render_to_response('article.html', {'article': Article.objects.get(id=article_id), 'comments': Comments.objects.filter(comments_article_id=article_id)})
