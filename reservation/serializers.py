from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    seat_number = serializers.CharField(source='seat.seat_number', read_only=True)
    seat_price = serializers.DecimalField(source='seat.price', max_digits=8, decimal_places=2, read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'movie', 'seat', 'movie_title', 'seat_number', 'seat_price', 'reserved_at']
        extra_kwargs = {
            'movie' : {'write_only':True},
            'seat' : {'write_only':True},
        }

    def validate(self, data):
        seat = data['seat']
        movie = data['movie']
        if movie.sold_out:
            raise serializers.ValidationError("movie sold out!")
        if Ticket.objects.filter(seat=seat).exists():
            return serializers.ValidationError('seat already reserved!')
        if seat.movie != movie:
            raise serializers.ValidationError('The chair does not belong in this film!')
        return data

    def create(self, validated_data):
        user = self.context['request'].user
        return Ticket.objects.create(user=user, **validated_data)
