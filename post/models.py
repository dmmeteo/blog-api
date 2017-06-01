from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)  # "auto_now" means saved(updated) object
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)  # "auto_now_add" means initial(create) object
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='post_add')
    last_edit_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='post_edit')
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-timestamp', '-updated']

    def __unicode__(self):  # python2
        return self.title

    def __str__(self):  # python3
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})


def pre_save_post(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    instance.slug = slug

pre_save.connect(pre_save_post, sender=Post)
