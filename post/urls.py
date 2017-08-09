from __future__ import unicode_literals

from django.conf.urls import url, include
from views import *
from rest_framework.routers import DefaultRouter


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'api', PostViewSet)

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^create/$', PostCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[-\w]*)/detail/$', PostDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[-\w]*)/update/$', PostUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[-\w]*)/delete/$', PostDeleteView.as_view(), name='delete'),
    
    # API
    url(r'^', include(router.urls)),
]
