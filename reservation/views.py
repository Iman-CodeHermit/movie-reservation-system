from .serializers import TicketSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Ticket

# Create your views here.
class ReservationTicketView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        serializer = TicketSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            ticket = serializer.save()
            return Response(TicketSerializer(ticket).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, ticket_id):
        try:
            ticket = Ticket.objects.get(id=ticket_id, user=request.user)
        except Ticket.DoesNotExist:
            return Response({"error": "ticket not found"}, status=404)

        if ticket.payment_status == 'paid':
            return Response({"message": "This ticket has already been paid!"}, status=400)

        if ticket.movie.sold_out:
            return Response({"error": "movie sold out"}, status=400)

        ticket.payment_status = 'paid'
        ticket.save()

        ticket.movie.check_sold_out()

        return Response({
            "message": "پرداخت موفقیت‌آمیز بود.",
            "ticket_id": ticket.id,
            "seat": ticket.seat.seat_number,
            "movie": ticket.movie.title
        })


