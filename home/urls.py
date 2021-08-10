from django.urls import path, re_path, include
from .views import UserCreation, CarCollection, CarDetails, GpsCollection, NewCarCollection
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login', obtain_auth_token),
    path('register', UserCreation.as_view()),
    path('cars', CarCollection.as_view()),
    path('cars/<int:pk>/', CarDetails.as_view()),
    path('cars/<int:pk>/gps', GpsCollection.as_view()),
    path('newcars', NewCarCollection.as_view()),
]
