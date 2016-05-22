from django.conf.urls import url
from portfolio.blog.views import (blog, about, portfolio,
                                  entry, entries_with_given_tag, search_results)


urlpatterns = [
    url(r'^$', blog, name='blog'),
    url(r'^about/?$', about, name='about'),
    url(r'^porfolio/?$', portfolio, name='portfolio'),
    url(r'^entry/(?P<pk>\d+)/?$', entry, name='entry'),
    url(r'^entries/(?P<tag_name>\w+)/?$', entries_with_given_tag, name='entries_with_given_tag'),
    url(r'^entries/search/?', search_results, name='search_results'),
]
