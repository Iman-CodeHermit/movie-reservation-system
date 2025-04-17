from django.contrib import admin
from .models import Director, Actor, Movie, Comment
# Register your models here.

admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Comment)