from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = ['parcel_name','tracking_number','status','recipient_name','sender_name', 'status']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # Prevent password from being returned
        }

    def create(self, validated_data):
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data['password'])
        return CustomUser.objects.create(**validated_data)