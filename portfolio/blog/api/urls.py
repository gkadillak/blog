from django.conf.urls import url
from .views.entry import EntryView

urlpatterns = [
    url(r'entries/$', EntryView.as_view()),
]
