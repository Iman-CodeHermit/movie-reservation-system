from rest_framework import serializers
from movie.models import Movie

class AvailableMoviesView(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'summary', 'sold_out']
