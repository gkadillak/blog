from portfolio.blog.models import Entry
from rest_framework import serializers
from .tag import TagSerializer


class EntrySerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Entry
