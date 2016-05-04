from __future__ import unicode_literals

from django.db import models

class TimeStampMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(TimeStampMixin):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Entry(TimeStampMixin):
    body = models.TextField()
    headline = models.CharField(max_length=120)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.headline
