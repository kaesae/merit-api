from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..serializers.post import PostSerializer
from ..models.post import Post
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied


class PostsView(APIView):
    def get(self, request):
        posts = Post.objects.filter(author=request.user.id)
        data = PostSerializer(posts, many=True).data
        return Response(data)

    def post(self, request):
        request.data['author'] = request.user.id
        post = PostSerializer(data=request.data)
        if post.is_valid():
            post.save()
            return Response(post.data, status=status.HTTP_201_CREATED)
        else:
            return Response(post.errors, status=status.HTTP_400_BAD_REQUEST)

class PostView(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.user != post.author:
            raise PermissionDenied('Unauthorized, you do not own this post')
        data = PostSerializer(post).data
        return Response(data)