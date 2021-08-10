from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.db.models.signals import post_save
from django.dispatch import receiver


class Organization(models.Model):
    name = models.CharField(max_length=255)
    nip = models.PositiveIntegerField()
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    street_num = models.CharField(max_length=10)
    postal_code = models.PositiveIntegerField()
    admin = models.ForeignKey(User, null=True, on_delete=SET_NULL)

    def __str__(self) -> str:
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    org = models.ForeignKey(Organization, null=True, on_delete=models.RESTRICT)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)  # add this
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return str(self.user)


class Car(models.Model):
    owner = models.ForeignKey(
        Organization, related_name='cars', on_delete=models.CASCADE, default=1)
    driver = models.OneToOneField(
        Profile, null=True, blank=True, on_delete=models.RESTRICT)
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
