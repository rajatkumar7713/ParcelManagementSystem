from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = ['tracking_number', 'sender_name', 'parcel_name', 'recipient_name', 'status']
        read_only_fields = ['tracking_number']  
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  
        }

    def create(self, validated_data):
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data['password'])
        return CustomUser.objects.create(**validated_data)