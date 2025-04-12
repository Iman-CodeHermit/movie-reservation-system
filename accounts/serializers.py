from rest_framework import serializers
from .models import User


class UserRegiterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name', 'password1', 'password2')
        extra_kwargs = {
            'email': {'required': True},
            'full_name': {'required': True},
            'password1':{'required: True'},
            'password2': {'required: True'}
        }

        def validate(self, data):
            if data['password1'] and data['password2'] and data['password1'] != data['password2']:
                raise serializers.ValidationError('passwords must match!')
            return data
