from rest_framework import serializers
from .models import Car, Gps


class CarSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
