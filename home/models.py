from io import SEEK_END
from django.db import models
from datetime import datetime, date
#from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractUser


class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    nip = models.PositiveIntegerField(
        unique=True, validators=[MaxValueValidator(9999999999)])
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    street_num = models.CharField(max_length=10)
    postal_code = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name


class User(AbstractUser):
    PERMISSION = (
        ('0', 'User'),
        ('9', 'Admin')
    )
    organization = models.ForeignKey(
        Organization, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    organization_permission = models.CharField(
        choices=PERMISSION, blank=True, null=True, default=None, max_length=1, verbose_name='Acces level')


class Car(models.Model):
    owner = models.ForeignKey(
        Organization, related_name='cars', on_delete=models.CASCADE)
    driver = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    token = models.CharField(
        max_length=32, null=False)
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

class CarService(models.Model):
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    street_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Attachments(models.Model):
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Maintenance(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(CarService, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    mileage = models.PositiveIntegerField(null=False)
    date = models.DateField(null=False)



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
