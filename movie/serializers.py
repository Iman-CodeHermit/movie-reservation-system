from rest_framework import serializers
from .models import Comment, Director, Actor, Movie
from reservation.models import Ticket


class CommentSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'movie', 'movie_title', 'text', 'rating', 'created_at']
        extra_kwargs = {
            'movie' : {'write_only':True},
            'text' : {'required':True},
            'rating' : {'required':True},
        }

        def validate_rating(self, value):
            if value < 1 or value > 5:
                return serializers.ValidationError('rating must be between 1 and 5')
            return value

        def validate(self, data):
            user = self.context['request'].user
            movie = data['movie']
            if not Ticket.objects.filter(user=user, movie=movie).exists():
                return serializers.ValidationError('you do not have access add comment for this movie because dont reserved')
            return data

        def create(self, validated_data):
            user = self.context['request'].user
            return Comment.objects.create(user=user, **validated_data)

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name']

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name']

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    actors = ActorSerializer()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'summary', 'director', 'actors', 'sold_out']
