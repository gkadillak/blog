from django.conf.urls import url
from .views import bio, portfolio, home, post

urlpatterns = [
    url(r'bio/?$', bio, name='bio'),
    url(r'portfolio/?$', portfolio, name='projects'),
    url(r'post/(?P<id>\d+)/?$', post, name='post'),
    url(r'$', home, name='home'),
]
