from django.db import models
from django.utils.text import slugify
import time
from .utils import create_photo_directory


class TimeStampModel(models.Model):
    """
    An abstract base class model that provides
    self-updating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampModel):
    body = models.TextField()
    headline = models.CharField(max_length=140)
    published = models.BooleanField(default=True)
    slug = models.SlugField()

    def create_photo_directory(self):
        return create_photo_directory(self.headline)

    def save(self, *args, **kwargs):
        self.create_photo_directory()
        self.slug = slugify(self.headline)
        super().save(*args, **kwargs)

    def __str__(self):
        return time.strftime('{0}: %A, %B %e %G'.format(self.headline))
