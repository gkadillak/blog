from django.conf.urls import url

from . import views

app_name = 'webhooks'

urlpatterns = [
    url(r'^deploy/?$', views.deploy),
]
