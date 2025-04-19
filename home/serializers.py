from rest_framework import serializers
from movie.models import Movie

class AvailableMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'summary', 'sold_out']
