#-*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Categorie(models.Model):
    """ Stores table categorie, for articles with fields below"""
    class Meta():
        db_table = 'categories'
    cat_title = models.CharField(max_length=20)
    cat_description = models.TextField()
    cat_url = models.CharField(max_length=200)
    cat_disabled = models.BooleanField(default=False)
    def __unicode__(self):
        return self.cat_title

class Article(models.Model):
    """ Stores table Article with fields below"""
    class Meta():
        db_table = 'articles'
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)    # or we can use blank=true, null=true
    article_disabled = models.BooleanField(default=False)
    article_categorie = models.ForeignKey(Categorie)
    def __unicode__(self):
        return self.article_title


class Comment(models.Model):
    """ Stores table Comment, for articles with fields below"""
    class Meta():
        db_table = 'comments'
    comments_text = models.TextField(verbose_name=u"Текст комментария")
    comments_article = models.ForeignKey(Article)
    def __unicode__(self):
        return self.comments_text