from __future__ import unicode_literals

from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
