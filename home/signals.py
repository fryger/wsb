from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Car, CarDriversHistory, User


@receiver(pre_save, sender=Car)
def driverHistory(sender, instance, **kwargs):
    if instance.driver is not None:
        carInstance = Car.objects.get(id=instance.id)
        log = CarDriversHistory(
            car=carInstance,
            driver=User.objects.get(username=instance.driver),
            mileage=carInstance.mileage)
        log.save()
