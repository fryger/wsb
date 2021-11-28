from .scheduler import scheduler
from datetime import datetime
import time as tim
from .models import Car, Gps, User
from datetime import timedelta
from .sms import sms

############ config ############

coolant_temp_threshold = 100
speed_threshold = 10

################################


def param_monitor(car, parameter, message):
    data = []
    first_val = Gps.objects.filter(car=car).values_list(
        parameter, 'datetime', 'speed').order_by('-id')[0]
    data.append(first_val)
    for t in range(30):
        instance = Gps.objects.filter(car=car).values_list(
            parameter, 'datetime', 'speed').order_by('-id')[0]
        tim.sleep(1)
        if data[-1][1] != instance[1]:
            data.append(instance)
    if data[-1][2] > speed_threshold:
        param_mean = round(sum(map(lambda x: x[0], data)) / len(data))
        if param_mean > first_val[0]:
            if Car.objects.get(name=car).driver is not None:
                sms(Car.objects.get(name=car).driver.phone, {
                    'title': "Car guardian: ", "description": (message[0] + str(param_mean))})
                print("Driver")
            else:
                sms(User.objects.get(organization=Car.objects.get(
                    name=car).owner, organization_permission='9').phone, {'title': "Car guardian: ", "description": (message[1] + str(param_mean))})
                print("Suppervisior")
    # tim.sleep(600)


def car_guardian(data):
    car = Car.objects.get(name=data['car'])

    if data['colanttemp'] >= coolant_temp_threshold:
        parameter = 'colanttemp'
        message = ["Possible engine overheat on your car, please stop and cool your engine. Coolant mean temperature: ",
                   f"Possible engine overheat, on car {car.name}, please contact with driver. Coolant mean temperature: "]

        scheduler.add_job(param_monitor, id=(
            car.name + parameter), args=[car, parameter, message])


'''
speed_threshold = 10
temp_threshold = 90
guarded_objects = Car.objects.all()
querry_period = datetime.now() - timedelta(minutes=5)
parameter = "colanttemp"
def organizationGuardian(parameter, querry_period, guarded_objects, temp_threshold):
    for car in guarded_objects:
        records = Gps.objects.exclude(colanttemp__isnull=True).filter(
            speed__gte=10,
            car=car,
            datetime__range=(
                querry_period,
                datetime.now())).values_list(parameter)
        if len(records) != 0:
            mean = round(sum(map(lambda x: x[0], records)) / len(records))
            if mean >= temp_threshold:
                scheduler.add_job(param_monitor, id=(
                    car.name + parameter), args=[car, parameter, mean])


if scheduler.get_job('organizationGuardian'):
    scheduler.remove_job("organizationGuardian")
    scheduler.add_job(organizationGuardian, 'interval',
                      id="organizationGuardian", minutes=5, args=[parameter, querry_period, guarded_objects, temp_threshold])
else:
    scheduler.add_job(organizationGuardian, 'interval',
                      id="organizationGuardian", minutes=5, args=[parameter, querry_period, guarded_objects, temp_threshold])
'''
