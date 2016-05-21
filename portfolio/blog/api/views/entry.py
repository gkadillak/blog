from rest_framework import filters
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (ListModelMixin,
                                   RetrieveModelMixin)
from portfolio.blog.models import Entry
from portfolio.blog.api.serializers.entry import EntrySerializer


class EntryView(GenericAPIView, ListModelMixin, RetrieveModelMixin):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('body', 'headline', 'tags__name')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
