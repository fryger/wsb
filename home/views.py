from .scheduler import scheduler
from .tasks import set_scheduler
from datetime import date, datetime
import dateutil.parser
from django.db.models.query import QuerySet
from django.http import HttpResponse, JsonResponse, request
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django_filters import rest_framework as filters
from rest_framework import generics, mixins, status, viewsets
from rest_framework import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.fields import SerializerMethodField
from rest_framework.filters import SearchFilter
from rest_framework.parsers import JSONParser
from rest_framework.permissions import OR, AllowAny, IsAuthenticated, DjangoModelPermissions, DjangoObjectPermissions
from .permissions import BaseDjangoModelPermissions
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .decorators import have_orgization
from .models import Attachments, Car, CarPicture, Maintenance, Organization, Reminders, User, Gps, CarDriversHistory, CarDamages, CarDamagesAttachment
from .serializers import CarLatestPointSerializer, ReminderCollectionSerializer, UserSerializer, OrganizationSerializer, ProfileSerializer, DriverSerializer, DriverPasswordSerializer, CarSerializer, GpsSerializer, MaintenanceSerializer, MaintenanceDetailSerializer, MyFileSerializer, OrganizationCreationSerializer, CarPictureSerializer, CarDriversHistorySerializer, CarDamagesSerializer

from .guardian import *


class TestAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):

        return Response(status=status.HTTP_200_OK)


class UserCreation(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationCreationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = OrganizationCreationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationCollection(mixins.ListModelMixin, mixins.CreateModelMixin,
                             mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = OrganizationSerializer

    def get_queryset(self):
        return Organization.objects.filter(id=self.request.user.organization.id)

    def get_object(self):
        return Organization.objects.get(pk=self.request.user.organization.id)

    def perform_create(self, serializer):
        serializer = serializer.save()
        user = User.objects.get(id=self.request.user.id)
        user.organization = serializer
        user.organization_permission = 9
        user.save()
        return serializer

    def perform_destroy(self, instance):
        user = User.objects.get(id=self.request.user.id)
        user.organization_permission = 0
        user.save()
        return super().perform_destroy(instance)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @method_decorator(have_orgization())
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if self.request.user.organization_permission == '9':
            return self.update(request, *args, **kwargs)
        else:
            return HttpResponse("Unauthorized", status=401)

    def delete(self, request, *args, **kwargs):
        if self.request.user.organization_permission == '9':
            return self.destroy(request, *args, **kwargs)
        else:
            return HttpResponse("Unauthorized", status=401)


class UserDetail(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                 generics.GenericAPIView):

    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_object(self):
        return User.objects.get(pk=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class DriverCollection(mixins.ListModelMixin, mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin, generics.GenericAPIView):

    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [BaseDjangoModelPermissions]
    serializer_class = DriverSerializer

    def get_queryset(self):
        return User.objects.filter(organization=self.request.user.organization)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            driver = serializer.save()
            driver.organization = self.request.user.organization
            driver.organization_permission = 0
            driver.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DriverDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin, generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = DriverSerializer

    def get_queryset(self):
        return User.objects.filter(organization=self.request.user.organization)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UpdateDriverPassword(mixins.UpdateModelMixin, generics.GenericAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = DriverPasswordSerializer

    def get_queryset(self):
        return User.objects.filter(organization=self.request.user.organization)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CarCollection(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CarSerializer

    def get_queryset(self):
        if self.request.user.organization_permission == '9':
            return Car.objects.filter(owner=self.request.user.organization)
        else:
            return Car.objects.filter(owner=self.request.user.organization, driver=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # Zablokować dla adminów organizacji
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# Zablokować dla adminów organizacji


class CarDetail(mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                mixins.UpdateModelMixin, generics.GenericAPIView):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user.organization)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if Car.objects.get(id=kwargs['pk']).owner == self.request.user.organization:
            return self.update(request, *args, **kwargs)
        else:
            return HttpResponse("Wrong driver id", status=404)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CarDriverHistoryCollection(mixins.ListModelMixin, generics.GenericAPIView):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CarDriversHistorySerializer

    def get_queryset(self):
        if self.request.user.organization_permission == '9':
            queryset = CarDriversHistory.objects.filter(car=Car.objects.get(id=self.kwargs['pk'],
                                                                            owner=self.request.user.organization))
        else:
            queryset = CarDriversHistory.objects.filter(car=Car.objects.get(id=self.kwargs['pk'],
                                                                            owner=self.request.user.organization,
                                                                            driver=self.request.user))
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GpsCollection(mixins.ListModelMixin, generics.GenericAPIView):

    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = GpsSerializer

    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    filterset_fields = ['datetime']
    search_fields = ['datetime']

    def get_queryset(self):
        queryset = None

        start_date = self.request.query_params.get('from')
        end_date = self.request.query_params.get('to')

        if self.request.user.organization_permission == '9':
            queryset = Gps.objects.filter(car=Car.objects.get(id=self.kwargs['pk'],
                                                              owner=self.request.user.organization))
        else:
            queryset = Gps.objects.filter(car=Car.objects.get(id=self.kwargs['pk'],
                                                              owner=self.request.user.organization,
                                                              driver=self.request.user))

        if (start_date is not None) and (start_date != ""):
            queryset = queryset.filter(datetime__gte=start_date)

        if (end_date is not None) and (end_date != ""):
            queryset = queryset.filter(datetime__lte=end_date)

        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# walidacja czy to jest właściciel
#    def post(self, request, *args, **kwargs):
#        return self.create(request, *args, **kwargs)


class GpsPointCreation(mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = GpsSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GpsPointsLatest(generics.GenericAPIView, mixins.ListModelMixin):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CarLatestPointSerializer

    def get_queryset(self):

        return Car.objects.filter(owner=self.request.user.organization)
        if self.request.user.organization_permission == '9':
            return Gps.objects.filter(car=Car.objects.filter(
                owner=self.request.user.organization)).latest('datetime')
        else:
            return Gps.objects.filter(car=Car.objects.filter(
                owner=self.request.user.organization,
                driver=self.request.user)).latest('datetime')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GpsPointLatest(generics.GenericAPIView, mixins.RetrieveModelMixin):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = GpsSerializer

    def get_object(self, *args, **kwargs):
        if self.request.user.organization_permission == '9':
            return Gps.objects.filter(car=Car.objects.get(id=self.kwargs['pk'],
                                                          owner=self.request.user.organization)).latest('datetime')
        else:
            return Gps.objects.filter(car=Car.objects.get(id=self.kwargs['pk'],
                                                          owner=self.request.user.organization,
                                                          driver=self.request.user)).latest('datetime')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class MaintenanceCollection(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MaintenanceSerializer

    def get_queryset(self):
        return Maintenance.objects.filter(car=Car.objects.get(id=self.kwargs['pk']))

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MaintenanceDetails(mixins.RetrieveModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MaintenanceDetailSerializer

    def get_object(self):
        return Maintenance.objects.get(pk=self.kwargs['pk2'])

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# validacja czy samochód należy do organizacji zgłaszającgo (jak w get)


class CarDamagesCollection(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    authentication_classes = [TokenAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CarDamagesSerializer

    def get_queryset(self):
        return CarDamages.objects.filter(car=Car.objects.get(id=self.kwargs['pk']))

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CarPictureView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None, *args, **kwargs):
        if Car.objects.get(id=kwargs['pk']).owner == self.request.user.organization:
            galery = CarPicture.objects.filter(car=kwargs['pk'])
            serializer = CarPictureSerializer(galery, many=True)
            return Response(serializer.data)
        else:
            return HttpResponse("", status=404)

    def post(self, request, *args, **kwargs):
        request.data.update({'car': kwargs['pk']})
        file_serializer = CarPictureSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        snippet = CarPicture.objects.filter(car=kwargs['pk'], id=kwargs['pk2'])
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MyFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = MyFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        set_scheduler()
        return Response("Done")


class RemindersCollection(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ReminderCollectionSerializer

    def get_queryset(self):
        return Reminders.objects.filter(car=Car.objects.get(id=self.kwargs['pk']))

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
