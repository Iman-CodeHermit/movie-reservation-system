from django.template.context_processors import request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User
from .serializers import UserRegiterSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout

# Create your views here.

class UserRegisterView(APIView):
    def post(self, request):
        ser_data = UserRegiterSerializer(data=request.data)
        if ser_data.is_valid():
            User.objects.creat_user(
                email = ser_data.validated_data['email'],
                phone_number= ser_data.validated_data['phone_number'],
                full_name = ser_data.validated_data['full_name'],
                password = ser_data.validated_data['passwoed1'],
            )
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)