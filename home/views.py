from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Car, Gps
from .serializers import CarSerialzer, GpsSerializer, UserSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


class UserCreation(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        cars = Car.objects.filter(owner=user)
        serializer = CarSerialzer(cars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CarSerialzer(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id, user):
        try:
            return Car.objects.get(id=id, owner=user)
        except Car.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        user = request.user
        car = self.get_object(id, user)
        serializer = CarSerialzer(car)
        return Response(serializer.data)

    def put(self, request, id, *args, **kwargs):
        user = request.user
        car = self.get_object(id, user)
        serializer = CarSerialzer(car, data=request.data)

        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        user = request.user
        car = self.get_object(id, user)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''
class GpsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        user = request.user
        gps = Gps.objects.filter(car=Car.objects.get(id=id, owner=user))
        serializer = GpsSerializer(gps, many=True)
        return Response(serializer.data)

    def post(self, request, id=None):
        user = request.user
        serializer = GpsSerializer(data=request.data)
        request.data['car'] = Car.objects.get(id=id, owner=user).id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
