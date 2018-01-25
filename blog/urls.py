from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/?', admin.site.urls),
    url(r'^', include('portfolio.urls', namespace='portfolio')),
    url(r'^wiki-edits/', include('wiki_edits.urls', namespace='wiki_edits')),
]

