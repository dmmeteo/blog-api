from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)  # "auto_now" means saved(updated) object
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)  # "auto_now_add" means initial(create) object

    class Meta:
        ordering = ['-timestamp', '-updated']

    def __unicode__(self):  # python2
        return self.title

    def __str__(self):  # python3
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
