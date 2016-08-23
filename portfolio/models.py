from django.db import models
import time


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

    def __str__(self):
        return time.strftime('{0}: %A, %B %e %G'.format(self.headline))


class Photo(models.Model):
    post = models.ForeignKey('Post', related_name='posts')
    photo = models.ImageField()
    description = models.CharField(max_length=140)

    def __str__(self):
        return time.strftime(time.strftime('{0}: %A, %B %e %G'.format(self.description)))
