from django.conf.urls import url
from .views import bio, portfolio, home

urlpatterns = [
    url(r'bio/$', bio, name='bio'),
    url(r'portfolio/$', portfolio, name='projects'),
    url(r'$', home, name='home'),
]
