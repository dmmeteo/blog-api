# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import pytz
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models


class User(AbstractUser):
    time_zone = models.CharField('Time zone', blank=True, max_length=255,
                                 choices=[[tz, tz] for tz in pytz.common_timezones])
    
    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
