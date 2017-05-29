from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list'),

    url(r'^create/$', PostCreateView.as_view(), name='post_create'),
    url(r'^(?P<pk>[\d]+)/detail/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^(?P<pk>[\d]+)/update/$', PostUpdateView.as_view(), name='post_update'),
    url(r'^(?P<pk>[\d]+)/delete/$', PostDeleteView.as_view(), name='post_delete'),
]