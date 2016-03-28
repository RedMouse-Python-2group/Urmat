from django.conf.urls import url
from article import views

urlpatterns = [
    url(r'^articles/all/$', 'article.views.articles'),
    url(r'^articles/get/(?P<id>\d+)/$', 'article.views.article'),
]