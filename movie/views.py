from rest_framework.response import Response
from rest_framework.views import APIView
from serializers import CommentSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CreateCommentView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        serializer = CommentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            comment = serializer.save()
            return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
