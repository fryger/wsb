from django.shortcuts import render
from django.http import HttpResponse
from .models import Car, Gps

def index(response, id):
    cars = Car.objects.get(id=id)
    path = cars.gps_set.all()
    return HttpResponse(f"<p>{cars.fname}</p><p>{[i.lat for i in path]}</p>")
