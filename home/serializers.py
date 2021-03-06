from home.guardian import car_guardian
from .tasks import set_scheduler
import uuid

from rest_framework import fields, serializers
from rest_framework.parsers import DataAndFiles
from .models import Attachments, CarDamages, CarDamagesAttachment, CarService, Organization, Reminders, User, Car, Gps, Maintenance, CarPicture, CarDriversHistory
from django.contrib.auth.password_validation import validate_password
# from django.contrib.auth.models import User


class DynamicFieldsModelSerializer(serializers.HyperlinkedModelSerializer):
    """
    A HyperlinkedModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)
        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        if exclude:
            # Drop fields that are specified in the `exclude` argument.
            excluded = set(exclude)
            for field_name in excluded:
                try:
                    self.fields.pop(field_name)
                except KeyError:
                    pass


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
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
        fields = ('username', 'email', 'organization',
                  'organization_permission')
        read_only_fields = ('orgnanization', 'organization_permission')


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class OrganizationCreationSerializer(serializers.ModelSerializer):

    class OrganizationTmpSerializer(serializers.ModelSerializer):
        class Meta:
            model = Organization
            fields = '__all__'

    organization = OrganizationTmpSerializer()

    class Meta:
        model = User
        fields = ('username', 'password', 'email',
                  'first_name', 'last_name', 'organization', 'organization_permission')
        read_only_fields = ['organization_permission', ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        data = validated_data.pop('organization')
        organization = Organization(**data)
        organization.save()

        validated_data['organization'] = organization
        validated_data['organization_permission'] = '9'
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)

        user.save()

        return user


class DriverSerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name',
                  'last_name', 'organization_permission')


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


class CarDriversHistorySerializer(serializers.ModelSerializer):
    driver = DriverSerializer()

    class Meta:
        model = CarDriversHistory
        fields = ['driver', 'start_date', 'end_date',
                  'start_mileage', 'end_mileage']


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'
        read_only_fields = ['owner', 'token']

    def create(self, validated_data):
        if 'token' not in validated_data:
            validated_data['token'] = uuid.uuid1().hex
        if 'owner' not in validated_data:
            validated_data['owner'] = self.context['request'].user.organization
        return super(CarSerializer, self).create(validated_data)


class GpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gps
        fields = ('__all__')
        read_only_fields = ['car', 'id']

    def create(self, validated_data):

        validated_data['car'] = Car.objects.get(
            token=self.context['request'].META['HTTP_CAR'])
        car_guardian(validated_data)
        return super(GpsSerializer, self).create(validated_data)


class CarGPSLatestPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gps
        fields = ("id", "lat", "lon", "alt", "speed", "datetime", )


class CarLatestPointSerializer(serializers.ModelSerializer):
    # gps_set = GpsSerializer(many=True, read_only=True)
    gps = serializers.SerializerMethodField()
    driver = DriverSerializer()

    class Meta:
        model = Car
        fields = ("id", "name", "gps", "driver")

    def get_gps(self, obj):
        gps = obj.gps_set.last()
        response = CarGPSLatestPointSerializer(gps).data
        return response


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = ('title', 'mileage', 'date', 'shop')

    def create(self, validated_data):
        car = Car.objects.get(id=self.context.get(
            'request').parser_context.get('kwargs').get('pk'))
        validated_data['car'] = car
        validated_data['driver'] = car.driver
        return super().create(validated_data)


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarService
        fields = ('name', 'street', 'street_number')


class CarPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPicture
        fields = ('id', 'car', 'file')


class MyFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachments
        fields = ('file', 'uploaded_at', 'case')
        extra_kwargs = {'case': {'write_only': True}}


class CarDamagesFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDamagesAttachment
        fields = ('file', 'uploaded_at', 'name')
        extra_kwargs = {'case': {'write_only': True}}


class CarDamagesSerializer(serializers.HyperlinkedModelSerializer):
    shop = ShopSerializer(read_only=True)
    attachments = serializers.SerializerMethodField()

    class Meta:
        model = CarDamages
        fields = ('title', 'date', 'place', 'guilty', 'repaired',
                  'shop', 'insurance', 'damages', 'description', 'attachments')
        depth = 1

    def get_attachments(self, obj):
        attachments = obj.cardamagesattachment_set.all()
        response = CarDamagesFileSerializer(attachments, many=True).data
        return response

    def create(self, validated_data):
        shop = CarService.objects.get(
            id=self.context.get('request')._data['shop'])
        car = Car.objects.get(id=self.context.get(
            'request').parser_context.get('kwargs').get('pk'))
        validated_data['car'] = car
        validated_data['shop'] = shop
        return super().create(validated_data)


class MaintenanceDetailSerializer(serializers.HyperlinkedModelSerializer):
    driver = DriverSerializer(read_only=True, exclude=('id',))
    shop = ShopSerializer(read_only=True)
    attachments = serializers.SerializerMethodField()

    class Meta:
        model = Maintenance
        fields = ('title', 'description', 'mileage',
                  'driver', 'shop', 'date', 'attachments')
        depth = 1

    def get_attachments(self, obj):
        attachments = obj.attachments_set.all()
        response = MyFileSerializer(attachments, many=True).data
        return response


class ReminderCollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reminders
        fields = ('title', 'description', 'when', 'sms', 'email')

    def create(self, validated_data):

        car = Car.objects.get(id=self.context.get(
            'request').parser_context.get('kwargs').get('pk'))
        task = set_scheduler(
            car.driver.email, car.driver.phone, validated_data)

        validated_data['car'] = car
        validated_data['task'] = task
        return super().create(validated_data)
