from django.conf.urls import url
from .views import bio, portfolio, home, post, ssl_challenge


urlpatterns = [
    url(r'^bio/?$', bio, name='bio'),
    url(r'^portfolio/?$', portfolio, name='projects'),
    url(r'^post/(?P<slug>[-\w]+)/?$', post, name='post'),
    url(r'.well-known/acme-challenge/(?P<challenge>[\S]+)', ssl_challenge, name='ssl_challenge'),
    url(r'^$', home, name='home'),
]
