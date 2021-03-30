from django.db import models
from datetime import datetime

class Car(models.Model):
    fname = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    mileage = models.PositiveIntegerField()
    vin = models.CharField(max_length=17)

    def __str__(self):
        return self.fname

class Gps(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    datetime = models.DateTimeField(default=datetime.now)
