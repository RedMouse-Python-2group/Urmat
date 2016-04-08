from django.conf.urls import url, patterns

urlpatterns = [
    url(r'^login/$', 'users.views.login'),
    url(r'^logout/$', 'users.views.logout'),
    url(r'^registration/$', 'users.views.registration'),
]