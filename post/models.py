from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from datetime import datetime
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

    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.slug:
                self.slug = slugify(
                    '%s-%s' % (self.title, datetime.now())
                )

        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


# bad pre_save
# def pre_save_post(sender, instance, *args, **kwargs):
#     pk = instance.pk
#     slug = slugify(instance.title)
#
# pre_save.connect(pre_save_post, sender=Post)