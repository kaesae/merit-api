from rest_framework import serializers
from ..models.post import Post
from .user import UserSerializer


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'created_at', 'updated_at')