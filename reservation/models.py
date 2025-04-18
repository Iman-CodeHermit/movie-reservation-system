from django.db import models
from accounts.models import User

# Create your models here.

class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.seat_number

class Ticket(models.Model):
    PAYMENT_STATUS = [
        ('pending', 'در انتظار پرداخت'),
        ('paid', 'پرداخت شده'),
        ('failed', 'ناموفق'),
        ('expired', 'منقضی شده'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey('movie.Movie', on_delete=models.CASCADE)
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='pending')

    def __str__(self):
        return f"{self.user.full_name} - {self.movie.title} - {self.seat.seat_number}"

    def is_paid(self):
        return self.payment_status == 'paid'

