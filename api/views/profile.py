from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..serializers.profile import ProfileSerializer
from ..models.profile import Profile
from django.core.exceptions import PermissionDenied

class ProfileView(APIView):
    def get(self, request):
        profile = profile.objects.filter(author=request.user.id)
        data = ProfileSerializer(profile, many=True).data
        return Response(data)

    def post(self, request):
        request.data['author'] = request.user.id
        profile = ProfileSerializer(data=request.data)
        if profile.is_valid():
            profile.save()
            return Response(profile.data, status=status.HTTP_201_CREATED)
        else:
            return Response(profile.errors, status=status.HTTP_400_BAD_REQUEST)
