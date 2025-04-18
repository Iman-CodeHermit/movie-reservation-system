from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from movie.models import Movie
from .serializers import HomePageSerializer

class AvailableMoviesView(APIView):
    def get(self, request):
        movies = Movie.objects.filter(sold_out=False)
        serializer = HomePageSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
