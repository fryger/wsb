from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Car, CarDriversHistory, User
from datetime import datetime


@receiver(pre_save, sender=Car)
def driverHistory(sender, instance, **kwargs):
    print(instance.mileage)
    carInstance = Car.objects.get(id=instance.id)
    if instance.driver is not None and instance.driver != carInstance.driver:
        prevInstance = CarDriversHistory.objects.filter(car=carInstance).last()
        if prevInstance is not None:
            prevInstance.end_date = datetime.now()
            prevInstance.end_mileage = instance.mileage
            prevInstance.save()

        curInstance = CarDriversHistory(
            car=carInstance,
            driver=User.objects.get(username=instance.driver),
            start_mileage=instance.mileage)
        curInstance.save()
