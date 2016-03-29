from django.conf.urls import url
from django.views.generic import TemplateView

from article.views import ArticlesList

urlpatterns = [
    url(r'^articles/$', ArticlesList.as_view()),
]