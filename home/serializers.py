from rest_framework import serializers
from .models import Car, Gps, Profile, Organization
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'name', 'manufacturer', 'model',
                  'mileage', 'vin', 'driver', 'owner')
        read_only_fields = ('id', 'owner')

    def create(self, validated_data):
        if 'owner' not in validated_data:
            validated_data['owner'] = self.context['request'].user.profile.org
        return super(CarSerializer, self).create(validated_data)


class GpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gps
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    #usera = UserSerializer(read_only=True)
    #usera = UserSerializer.CharField(source='User.name')
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('user', 'id')


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
        read_only_fields = ('id', 'admin')

    def create(self, validated_data):
        if 'admin' not in validated_data:
            validated_data['admin'] = self.context['request'].user
        return super(OrganizationSerializer, self).create(validated_data)
