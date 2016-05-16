from rest_framework import serializers
from portfolio.blog.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag

