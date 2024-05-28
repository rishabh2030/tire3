from rest_framework import generics,status
from users.models import CustomUser
from rest_framework.response import Response
from ..serializers.normal_user_registration_serializer import NormalUserRegistrationSerializer

class NormalUserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = NormalUserRegistrationSerializer
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            token, refresh_token = user.get_tokens()
            token = {"access_token": token,"refresh_token": refresh_token}
            return Response(token, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)