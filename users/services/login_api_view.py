from rest_framework import generics,status
from users.models import CustomUser
from django.contrib.auth import authenticate
from rest_framework.response import Response
from ..serializers.user_login_serializer import UserLoginSerializer

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, **serializer.validated_data)

        if user is not None:
            token, refresh_token = user.get_tokens()
            token = {"access_token": token,"refresh_token": refresh_token}
            return Response(token, status=status.HTTP_200_OK)
        
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)