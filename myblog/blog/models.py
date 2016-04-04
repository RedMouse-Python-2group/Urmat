from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Categorie(models.Model):
    class Meta():
        db_table = 'categories'
    cat_title = models.CharField(max_length=20)
    cat_description = models.TextField()
    cat_url = models.CharField(max_length=200)
    cat_disabled = models.BooleanField(default=False)

class Article(models.Model):
    class Meta():
        db_table = 'articles'
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)    # or we can use blank=true, null=true
    article_disabled = models.BooleanField(default=False)
    article_categorie = models.ForeignKey(Categorie)
"""
class Comment(models.Model):
    class Meta():
        db_table = 'comments'
    comments_text = models.TextField()
    comments_article = models.ForeignKey(Article)
"""