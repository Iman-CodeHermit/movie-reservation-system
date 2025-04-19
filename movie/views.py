from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CommentSerializer, MovieSerializer
from rest_framework import status
from .models import Movie
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class MovieDetailView(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateCommentView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        serializer = CommentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            comment = serializer.save()
            return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
