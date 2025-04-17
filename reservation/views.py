from .serializers import TicketSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ReservationTicketView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        serializer = TicketSerializer(data=request.data, ccontext={'request':request})
        if serializer.is_valid():
            ticket = serializer.save()
            return Response(TicketSerializer(ticket).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)