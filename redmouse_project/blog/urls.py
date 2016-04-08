
from django.conf.urls import url, patterns
from django.contrib import admin

from blog.views import ArticlesList

urlpatterns = [
    url(r'^$', 'blog.views.index'),
    url(r'^page/(\d+)/$', 'blog.views.index'),
    url(r'^articles/get/(?P<article_id>\d+)/$', 'blog.views.article'),
    url(r'^articles/addlike/(?P<article_id>\d+)/$', 'blog.views.addLike'),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'blog.views.addComment'),
    url(r'^create/$', 'blog.views.article_create'),
    url(r'^cbv/page/(\d+)/$', ArticlesList.as_view()),
]