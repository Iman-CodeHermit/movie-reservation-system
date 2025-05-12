from django.contrib import admin
from .models import Director, Actor, Movie, Comment
# Register your models here.

admin.site.register(Director)
admin.site.register(Actor)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')  # نمایش آیدی و فیلدهای دیگه
admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment)