from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..serializers.post import PostSerializer
from ..models.post import Post

class PostsView(APIView):
    def get(self, request):
        posts = Post.objects.filter(author=request.user.id)
        data = PostSerializer(posts, many=True).data
        return Response(data)