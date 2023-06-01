# from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from form.serializers import UserRegistrationSerializers, UserLoginSerilalizers
from django.contrib.auth import authenticate
from form.renderers import UserRenderer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializers = UserRegistrationSerializers(data = request.data)
        if serializers.is_valid():
            user = serializers.save()
            print('user:',user)
            # if user.exists():
            #     return Response(request, 'Email is already taken.')
            # user.save()
            token = get_tokens_for_user(user)
            return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializers = UserLoginSerilalizers(data = request.data)
        if serializers.is_valid(raise_exception=True):
            email = serializers.data.get('email')
            password = serializers.data.get('password')
            user = authenticate(email = email, password = password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token, 'msg':'login Successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'msg':'email or password is not valid'}, status=status.HTTP_404_NOT_FOUND)
