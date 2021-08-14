from io import SEEK_END
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator


class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    nip = models.PositiveIntegerField(
        unique=True, validators=[MaxValueValidator(9999999999)])
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    street_num = models.CharField(max_length=10)
    postal_code = models.PositiveIntegerField()
    admin = models.OneToOneField(
        User, null=True, blank=True, on_delete=SET_NULL)

    def __str__(self) -> str:
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    org = models.ForeignKey(Organization, null=True,
                            blank=True, on_delete=models.SET_NULL)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return str(self.user)


class Car(models.Model):
    owner = models.ForeignKey(
        Organization, related_name='cars', on_delete=models.CASCADE)
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


@receiver(post_save, sender=Organization)
def change_user_org(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.get(user=instance.admin)
        profile.org = instance
        profile.save()
