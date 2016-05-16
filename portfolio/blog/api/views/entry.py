from rest_framework import generics, filters
from portfolio.blog.models import Entry
from portfolio.blog.api.serializers.entry import EntrySerializer


class EntryView(generics.ListAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('body', 'headline', 'tags__name')
