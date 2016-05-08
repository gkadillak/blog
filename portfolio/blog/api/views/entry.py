from rest_framework import generics
from portfolio.blog.models import Entry
from portfolio.blog.api.serializers.entry import EntrySerializer

class EntryView(generics.ListAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
