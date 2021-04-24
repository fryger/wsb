from rest_framework import serializers
from .models import Car, Gps


class CarSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class GpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gps
        fields = '__all__'
