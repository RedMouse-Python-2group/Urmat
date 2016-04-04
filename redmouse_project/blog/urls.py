
from django.conf.urls import url, patterns
from django.contrib import admin
from .views import article_create


urlpatterns = [
    url(r'^create/$', article_create, name="create"),
]