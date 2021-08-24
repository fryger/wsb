from rest_framework import serializers
from .models import Organization, User
from django.contrib.auth.password_validation import validate_password
#from django.contrib.auth.models import User


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

class ProfileSerializer(serializers.ModelSerializer):
    organization = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = ('username', 'email','organization','organization_permission')
        read_only_fields = ('orgnanization', 'organization_permission')

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'email','organization_permission')

    

class DriverPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password']
        extra_kwargs = {'password': {'write_only': True}} 

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        instance.set_password(password)
        instance.save()
        return instance
    

'''
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgSettings
        fields = ('organization', 'user', 'permission')


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

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
        read_only_fields = ('id', 'admin')

    def create(self, validated_data):
        if 'admin' not in validated_data:
            validated_data['admin'] = self.context['request'].user
        return super(OrganizationSerializer, self).create(validated_data)
'''