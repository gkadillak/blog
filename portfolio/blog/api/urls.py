from django.conf.urls import url
from .views.entry import EntryView, EntriesView
from .views.tag import TagView


urlpatterns = [
    url(r'entries/$', EntriesView.as_view()),
    url(r'entries/(?P<pk>\d+)/?', EntryView.as_view()),
    url(r'tags/$', TagView.as_view()),
]
