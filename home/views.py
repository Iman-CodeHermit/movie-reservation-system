from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from movie.models import Movie
from .serializers import AvailableMoviesSerializer

class AvailableMoviesView(APIView):
    def get(self, request):
        search_query = request.query_params.get('search', '').strip()
        movies = Movie.objects.filter(sold_out=False)
        if search_query:
            movies = movies.filter(title__icontains=search_query)
        serializer = AvailableMoviesSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
