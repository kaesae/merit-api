from rest_framework import serializers
from ..models.profile import Profile
from .user import UserSerializer

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'title', 'content', 'author', 'created_at')