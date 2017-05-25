from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list'),

    url(r'^create/$', PostCreateView.as_view(), name='post_create'),
    url(r'^deteil/(?P<pk>[\d]+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^update/(?P<pk>[\d]+)/$', PostUpdateView.as_view(), name='post_update'),
    url(r'^delete/(?P<pk>[\d]+)/$', PostDeleteView.as_view(), name='post_delete'),
]