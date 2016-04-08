# -*- coding: utf-8 -*-
from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "article_title",
            "article_text",
            "article_disabled",
            "article_categorie",
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "comments_text",
        ]
