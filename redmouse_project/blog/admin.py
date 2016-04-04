#-*- coding:utf-8 -*-
from django.contrib import admin
from blog.models import Categorie, Article #, Comment

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Article)




"""
from django.contrib import admin
from blog.models import Categorie  #, Article, Comment

# Register your models here.
admin.site.register(Categorie)
class ArticleInline(admin.StackedInline):
    model = Comment
    extra = 2

class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date']
    inlines = [ArticleInline]
    list_filter = ['article_date']


admin.site.register(Comment)
admin.site.register(Article, ArticleAdmin)
"""