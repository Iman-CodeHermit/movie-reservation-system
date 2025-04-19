from django.db import models
from accounts.models import User
from django.apps import apps

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    actors = models.ForeignKey(Actor, on_delete=models.SET_NULL, null=True)
    sold_out = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='liked_movies', blank=True)

    def __str__(self):
        return self.title

    def like_count(self):
        return self.likes.count()

    def check_sold_out(self):
        seat = apps.get_model('reservation', 'Seat')
        ticket = apps.get_model('reservation', 'Ticket')
        total_seats = seat.objects.filter(movie=self).count()
        sold_tickets = ticket.objects.filter(movie=self, payment_status='paid').count()
        self.sold_out = sold_tickets >= total_seats
        self.save()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.full_name} - {self.movie.title} - {self.rating}"
