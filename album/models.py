from __future__ import unicode_literals

from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    track_name = models.TextField(max_length=100)
    lyrics = models.TextField()
    photo = models.ImageField(upload_to='img/', default='img/not-found.jpg')

    def __unicode__(self):
        return '%s' % self.title

    def __str__(self):
        return self.title
