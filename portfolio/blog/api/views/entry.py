from rest_framework import generics
from portfolio.blog.models import Entry
from portfolio.blog.api.serializers.entry import EntrySerializer
from rest_framework import filters


class EntryView(generics.ListAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_backends = (filters.SearchFilter)
    search_fields = ('body', 'headline', 'tags')
    filter_backends = (filters.SearchFilter,)
