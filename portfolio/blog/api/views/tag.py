from rest_framework import generics, filters
from portfolio.blog.models import Tag
from portfolio.blog.api.serializers.tag import TagSerializer


class TagView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'created', 'updated')
