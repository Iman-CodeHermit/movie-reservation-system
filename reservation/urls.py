from django.urls import path
from . import views

app_name = 'reservation'
urlpatterns = [
    path('reservatickt/', views.ReservationTicketView.as_view(), name= 'reserve_ticket'),
    path('payment/<ticket_id>/', views.PaymentAPIView.as_view(), name = 'payment'),
]