from django.conf.urls import url
from .views.entry import EntryView
from .views.tag import TagView


urlpatterns = [
    url(r'entries/(?P<pk>\d+)/?', EntryView.as_view()),
    url(r'entries/$', EntryView.as_view()),
    url(r'tags/$', TagView.as_view()),
]
