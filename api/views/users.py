from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from ..serializers.user import UserSerializer
from django.contrib.auth import authenticate, login

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

class SignIn(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:  
            login(request, user)
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            user.token = token.key
            user.save()
            return Response({
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'token': token.key
                }
            })
        else:
            return Response({ 'msg': 'The username and/or password is incorrect.' }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class ChangePassword(generics.UpdateAPIView):
    def patch(self, request):
        user = request.user
        old_password = request.data['passwords']['old']
        new_password = request.data['passwords']['new']

        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response({ 'msg': 'Password updated!' }, status=status.HTTP_204_NO_CONTENT)
        else: 
            return Response({ 'msg': 'The username and/or password is incorrect.' }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
