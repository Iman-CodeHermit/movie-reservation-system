from django.db import models
from accounts.models import User
from movie.models import Movie

# Create your models here.

class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.seat_number

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.full_name} - {self.movie.title} - {self.seat.seat_number}"


