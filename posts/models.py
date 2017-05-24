from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)  # "auto_now" means saved(updated) object
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)  # "auto_now_add" means initial(create) object

    def __unicode__(self):  # python2
        return self.title

    def __str__(self):  # python3
        return self.title
