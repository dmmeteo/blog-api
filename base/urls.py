from __future__ import unicode_literals

from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', BaseHomeView.as_view(), name='home'),
]
