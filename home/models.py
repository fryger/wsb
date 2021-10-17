from uuid import uuid1, uuid4
import os
from io import SEEK_END
from django.db import models
from datetime import datetime, date
#from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser


def get_file_path(instance, filename):
    #ext = filename.split('.')[-1]
    filename = "%s/%s/%s" % (uuid1().hex, uuid4().hex, filename)
    return filename


class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    nip = models.PositiveIntegerField(
        unique=True, validators=[MaxValueValidator(9999999999)])
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    street_num = models.CharField(max_length=10)
    postal_code = models.PositiveIntegerField()
    logo = models.ImageField(null=True, default=None)

    def __str__(self) -> str:
        return self.name


class User(AbstractUser):
    PERMISSION = (
        ('0', 'User'),
        ('9', 'Admin')
    )
    email = models.EmailField(unique=True)
    organization = models.ForeignKey(
        Organization, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    organization_permission = models.CharField(
        choices=PERMISSION, blank=True, null=True, default=None, max_length=1, verbose_name='Acces level')


class Car(models.Model):
    BODY = (
        ('Hatchback', 'Hatchback'),
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Sedan', 'Sedan'),
        ('Convertible', 'Convertible'),
        ('Estate', 'Estate'),
        ('VAN', 'VAN'),
        ('Coupe', 'Coupe')
    )
    STATUS = (
        ('In use', 'In use'),
        ('Free', 'Free'),
        ('Broken', 'Broken'),
        ('Service', 'Service'),
        ('Transport', 'Transport')
    )
    FUEL = (
        ('Petrol', 'Petrol'),
        ('BIO', 'BIO'),
        ('LPG', 'LPG'),
        ('Diesel', 'Diesel'),
        ('ELECTRIC', 'Electric'),
        ('Hybrid', 'Hybrid')
    )

    owner = models.ForeignKey(
        Organization, related_name='cars', on_delete=models.CASCADE)
    body = models.CharField(choices=BODY, max_length=11)
    driver = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    token = models.CharField(
        max_length=32, null=False)
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    mileage = models.PositiveIntegerField()
    vin = models.CharField(max_length=17)
    status = models.CharField(choices=STATUS, max_length=12)
    year = models.IntegerField(validators=[
        MinValueValidator(1886), MaxValueValidator(9999)])
    fuel = models.CharField(choices=FUEL, max_length=8)
    engine = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(50.0)])

    def __str__(self):
        return self.name


class CarPicture(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_file_path)


class Gps(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    lat = models.FloatField(null=True, blank=True,)
    lon = models.FloatField(null=True, blank=True,)
    alt = models.FloatField(null=True, blank=True,)
    speed = models.FloatField(null=True, blank=True,)
    rpm = models.IntegerField(null=True, blank=True,)
    kph = models.FloatField(null=True, blank=True,)
    engineload = models.IntegerField(null=True, blank=True,)
    colanttemp = models.IntegerField(null=True, blank=True,)
    fuelpressure = models.IntegerField(null=True, blank=True,)
    mainfoldpressure = models.IntegerField(null=True, blank=True,)
    intakeairtemp = models.IntegerField(null=True, blank=True,)
    mafrate = models.IntegerField(null=True, blank=True,)
    throttle = models.IntegerField(null=True, blank=True,)
    runtime = models.IntegerField(null=True, blank=True,)
    fuellevel = models.IntegerField(null=True, blank=True,)
    absload = models.IntegerField(null=True, blank=True,)
    oiltemp = models.IntegerField(null=True, blank=True,)
    fuelrate = models.IntegerField(null=True, blank=True,)
    torque = models.IntegerField(null=True, blank=True,)
    ctrlmodvoltage = models.IntegerField(null=True, blank=True,)
    datetime = models.DateTimeField(default=datetime.now)


class CarService(models.Model):
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    street_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Maintenance(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(CarService, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    mileage = models.PositiveIntegerField(null=False)
    date = models.DateField(null=False)


class Attachments(models.Model):
    case = models.ForeignKey(Maintenance, on_delete=CASCADE)
    file = models.FileField(upload_to=get_file_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)


'''
class User(AbstractUser):
    pass



class OrgSettings(models.Model):
    PERMISSION = (
        ('0','User'),
        ('9','Admin')
    )

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    permission = models.CharField(choices=PERMISSION, default=0, max_length=1)
    
    def __str__(self) -> str:
        return ('Permissions ' + self.user.username)

class Car(models.Model):
    owner = models.ForeignKey(
        Organization, related_name='cars', on_delete=models.CASCADE)
    driver = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    mileage = models.PositiveIntegerField()
    vin = models.CharField(max_length=17)

    def __str__(self):
        return self.name


class Gps(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    datetime = models.DateTimeField(default=datetime.now)


'''
