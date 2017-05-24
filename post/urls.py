from django.conf.urls import url
from views import *

urlpatterns = [
    # url(r'^$', '.home', name='home'),
    url(r'^$', PostListView.as_view(), name='post_list'),
]