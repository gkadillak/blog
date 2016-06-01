from __future__ import unicode_literals

from django.db import models
from django_extensions.db.fields import AutoSlugField


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
    tags = models.ManyToManyField(Tag, blank=True)
    published = models.BooleanField(default=False)
    preview = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='headline', max_length=100)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return '{}, ({})'.format(self.headline,
                                 self.created.strftime('%a, %Y/%m/%d'))
