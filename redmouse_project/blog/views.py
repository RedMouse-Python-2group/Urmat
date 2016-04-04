# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.response import TemplateResponse
from blog.models import Article
from .forms import ArticleForm


def index(request):
    return TemplateResponse(request, 'articles/all_articles.html', {'articles': Article.objects.all()})



def article(request, article_id=1):
    context = {}
    context.update(csrf(request))
    context['article'] = Article.objects.get(id=article_id)
    #context['comments'] = Comments.object.filter(comments.)
    return TemplateResponse(request, 'articles/one_article.html', {'article': Article.objects.all()})

def article_create(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return render(request, "articles/success_message.html", {'message': "Article successfully created ! Thank you"})
    else:
        context = {
            "form": form,
                }
        return render(request, "articles/form_article.html", context)