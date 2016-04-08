#-*- coding:utf-8 -*-
from django.contrib import admin
from blog.models import Categorie, Article, Comment

# Register your models here.
class CategorieAdmin(admin.ModelAdmin):
    list_filter = ['cat_title']

class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date', 'article_categorie']
    list_filter = ['article_date']

admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
