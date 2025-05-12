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
            comment = serializer.save(user=request.user)
            return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LikeMovieView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'detail': 'movie not found'}, status=status.HTTP_404_NOT_FOUND)
        user = request.user
        if movie.likes.filter(id=user.id).exists():
            movie.likes.remove(user)
            return Response({'liked': False}, status=status.HTTP_200_OK)
        else:
            movie.likes.add(user)
            return Response({'liked': True}, status=status.HTTP_200_OK)
