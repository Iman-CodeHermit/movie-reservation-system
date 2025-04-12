from rest_framework import serializers
from .models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

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

class UserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15, required=True)
    password = serializers.CharField(max_length=128, write_only=True, required=True)

    def validate_phone_number(self, value):
        if not value.startswith('09'):
            raise serializers.ValidationError("شماره تلفن باید با 09 شروع شود")

        if len(value) != 11:
            raise serializers.ValidationError("شماره تلفن باید 11 رقمی باشد")

        return value
