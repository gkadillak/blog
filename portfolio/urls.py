from django.conf.urls import url
from .views import bio, portfolio, home, post, ssl_challenge


app_name = 'portfolio'

urlpatterns = [
    url(r'^bio/?$', bio, name='bio'),
    url(r'^portfolio/?$', portfolio, name='projects'),
    url(r'^post/(?P<slug>[-\w]+)/?$', post, name='post'),
    url(r'^$', home, name='home'),
]
