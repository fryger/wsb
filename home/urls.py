from django.urls import path, re_path, include
from .views import UserCreation, CarCollection, CarDetails, GpsCollection
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('cars', CarCollection.as_view()),
    path('cars/<int:pk>/', CarDetails.as_view()),
    path('cars/<int:pk>/gps', GpsCollection.as_view()),
]
