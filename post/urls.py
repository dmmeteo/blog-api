from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list'),

    url(r'^create/$', PostCreateView.as_view(), name='post_create'),
    url(r'^deteil/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^update/$', PostUpdateView.as_view(), name='post_update'),
    url(r'^delete/$', PostDeleteView.as_view(), name='post_delete'),
]