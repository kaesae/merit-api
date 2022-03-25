from rest_framework.response import Response
from ..serializers.user import UserSerializer
from rest_framework import status, generics


class SignUp(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        new_user = UserSerializer(data=request.data)
        if new_user.is_valid():
            new_user.save()
            return Response({ 'user': new_user.data }, status=status.HTTP_201_CREATED)
        else:
            return Response(new_user.errors, status=status.HTTP_400_BAD_REQUEST)
