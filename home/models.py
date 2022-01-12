from uuid import uuid1, uuid4
import os
from io import SEEK_END
from django.db import models
from datetime import datetime, date
from django.db.models.base import Model
#from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


def get_file_path(instance, filename):
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
    phone = PhoneNumberField(null=True, blank=True, unique=True)


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
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid')
    )

    owner = models.ForeignKey(
        Organization, related_name='cars', on_delete=models.CASCADE)
    body = models.CharField(choices=BODY, max_length=11)
    driver = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    token = models.CharField(
        max_length=32, null=False)
    plate = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=255, unique=True)
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


class CarDriversHistory(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    driver = models.ForeignKey(User,  on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(null=True, blank=True)
    start_mileage = models.PositiveIntegerField()
    end_mileage = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.car.name + " - " + self.driver.username + " - " + str(self.start_date)


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


class CarDamages(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    place = models.CharField(max_length=255)
    guilty = models.CharField(max_length=255)
    repaired = models.CharField(max_length=255)
    shop = models.ForeignKey(CarService, on_delete=models.PROTECT)
    insurance = models.CharField(max_length=255)
    damages = models.CharField(max_length=500)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class CarDamagesAttachment(models.Model):
    case = models.ForeignKey(CarDamages, on_delete=CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to=get_file_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class CarDocuments(models.Model):
    car = models.ForeignKey(Car, on_delete=CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to=get_file_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Maintenance(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    shop = models.ForeignKey(CarService, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    mileage = models.PositiveIntegerField(null=False)
    date = models.DateField(null=False)


class Attachments(models.Model):
    case = models.ForeignKey(Maintenance, on_delete=CASCADE)
    file = models.FileField(upload_to=get_file_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Reminders(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    when = models.DateTimeField()
    sms = models.BooleanField(default=False)
    email = models.BooleanField(default=False)
    task = models.CharField(max_length=255, null=True)
    #repetetive = models.BooleanField(default=False)


class Documents(models.Model):
    organization = models.ForeignKey(Organization, on_delete=CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.CharField(max_length=500)
    file = models.FileField(upload_to=get_file_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class FuelPrices(models.Model):
    pb95 = models.CharField(max_length=3)
    pb98 = models.CharField(max_length=3)
    on = models.CharField(max_length=3)
    lpg = models.CharField(max_length=3)
    reported = models.DateTimeField(auto_now_add=True)
