from django.http import HttpResponse, JsonResponse, request
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django_filters import rest_framework as filters
from rest_framework import generics, mixins, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import SearchFilter
from rest_framework.parsers import JSONParser
from rest_framework.permissions import OR, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .decorators import is_org_admin_or_unauthorized
from .models import Car, Gps, Organization, Profile
from .serializers import (CarSerializer, GpsSerializer, OrganizationSerializer,
                          ProfileSerializer, UserSerializer)


class NewCarCollection(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CarSerializer

    def get_queryset(self):
        if self.request.user.profile.org.admin == self.request.user:
            return Car.objects.filter(owner=self.request.user.profile.org)
        else:
            return Car.objects.filter(driver=self.request.user.profile, owner=self.request.user.profile.org)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @method_decorator(is_org_admin_or_unauthorized())
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NewOrganizationCollection(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    serializer_class = OrganizationSerializer

    def get_queryset(self):
        return Organization.objects.filter(name=self.request.user.profile.org)

    def get_object(self):
        return Organization.objects.get(pk=self.request.user.profile.org.id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if self.request.user.profile.org is None:
            return self.create(request, *args, **kwargs)
        else:
            return HttpResponse('User have organization', status=404)

    @method_decorator(is_org_admin_or_unauthorized())
    def delete(self, request, *args, **kwargs):
        try:
            instance = Organization.objects.get(admin=request.user)
            instance.delete()
            return Response({"message": "Deleted successfuly"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message": "Delete fail"}, status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(is_org_admin_or_unauthorized())
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class NewProfileCollection(mixins.RetrieveModelMixin, generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.get(user=self.request.user)

    def get_object(self):
        return Profile.objects.get(pk=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class UserCreation(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarCollection(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CarDetails(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class GpsCollection(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    serializer_class = GpsSerializer
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    filterset_fields = ['datetime']
    search_fields = ['datetime']

    def get_queryset(self):
        return Gps.objects.filter(car=Car.objects.get(id=self.kwargs['pk'], owner=self.request.user))

    def create(self, request, *args, **kwargs):
        serializer = GpsSerializer(data=request.data)
        request.data['car'] = Car.objects.get(
            id=self.kwargs['pk'], owner=self.request.user).id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
