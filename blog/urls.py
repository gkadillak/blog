from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/?', admin.site.urls),
    url(r'^', include('portfolio.urls', namespace='portfolio')),
    url(r'^webhooks/', include('webhooks.urls', namespace='webhooks'))
]
