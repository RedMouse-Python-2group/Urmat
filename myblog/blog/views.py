# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from blog.models import Article


def index(request):
    return TemplateResponse(request, 'articles/all_articles.html', {'articles': Article.objects.all()})


def article(request, article_id=1):
    context = {}
    context.update(csrf(request))
    context['article'] = Article.objects.get(id=article_id)
    #context['comments'] = Comments.object.filter(comments.)
    return TemplateResponse(request, 'articles/one_article.html', {'article': Article.objects.all()})