from django.urls import path
from . import views

app_name = 'reservation'
urlpatterns = [
    path('reservatickt/', views.ReservationTicketView.as_view(), name= 'reserveticket'),
]