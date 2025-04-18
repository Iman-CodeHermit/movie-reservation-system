from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User
from .serializers import UserRegiterSerializer, UserLoginSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from reservation.models import Ticket
from movie.serializers import MovieSerializer

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
        ser_data = UserLoginSerializer(data=request.data)
        if ser_data.is_valid():
            phone_number = ser_data.validated_data.get('phone_number')
            password = ser_data.validated_data.get('password')
            user = authenticate(request, phone_number=phone_number, password=password)
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

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        tickets = Ticket.objects.filter(user=user, payment_status='paid')
        purchased_movies = list(set(ticket.movie for ticket in tickets))
        liked_movies = user.liked_movies.all()
        purchased_serializer = MovieSerializer(purchased_movies, many=True, context={'request': request})
        liked_serializer = MovieSerializer(liked_movies, many=True, context={'request': request})
        return Response({'full_name': user.full_name, 'purchased_movies': purchased_serializer.data, 'liked_movies': liked_serializer.data, }, status=status.HTTP_200_OK)
