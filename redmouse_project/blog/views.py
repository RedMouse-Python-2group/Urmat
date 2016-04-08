# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from blog.models import Article, Comment, Categorie
from .forms import ArticleForm, CommentForm
from django.core.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator

#start CBV mode
from django.views.generic import TemplateView, ListView, DetailView

class AboutView(TemplateView):
    """ Static page About me """
    template_name = "about.html"

class ArticlesList(ListView):
    """ Main class for main page"""
    model = Article
    page_number=1
    current_page = Paginator(model, 4)
    template_name = "articles/article_list.html"

    def get_context_data(self, **kwargs):
        """ Function gets additional context """
        context = super(ArticlesList, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        context['popular_articles'] = Article.objects.order_by('-article_likes')[:10]
        return context

class ArticleDetail(DetailView):
    pass
#End CBV

def index(request, page_number=1):
    """ Main page function """
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 4)
    return render(request, 'articles/all_articles.html', {'articles': current_page.page(page_number), 'user': auth.get_user(request).username})

def article(request, article_id=1):
    """ Function renders article detail """
    context = {}
    context.update(csrf(request))
    context['article'] = Article.objects.get(id=article_id)
    context['comments'] = Comment.objects.filter(comments_article_id=article_id)
    context['form'] = CommentForm
    context['user'] = auth.get_user(request).username
    return render(request, "articles/one_article.html", context)

def addLike(reques, article_id=1):
    """ Function that allows to add likes """
    try:
        article = Article.objects.get(id=article_id)
        article.article_likes += 1
        article.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')

def addComment(request, article_id=1):
    """ Comment form appears under current article """
    if request.POST and ("spam" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)      # Allows you to create comment only after 60 sec
            request.session['spam'] = True
    return redirect('/articles/get/%s/' % article_id)

def article_create(request):
    """ Function creates article """
    if not request.user.is_authenticated():
        return redirect("/")
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