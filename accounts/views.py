
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User
from .serializers import UserRegiterSerializer, UserLoginSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from django.contrib.auth import aauthenticate
from rest_framework_simplejwt.tokens import RefreshToken

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

class UserLoginView(APIView):
    def post(self, request):
        phone_number = request.data

class UserLoginView(APIView):
    def post(self, request):
        ser_data = UserLoginSerializer(data=request.data)
        if ser_data.is_valid():
            phone_number = ser_data.validated_data.get('phone_number')
            password = ser_data.validated_data.get('password')
            user = aauthenticate(request, phone_number=phone_number, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token)
                    }, status= status.HTTP_200_OK
                )
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
