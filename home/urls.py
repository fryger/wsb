from django.urls import path, re_path, include
from .views import NewProfileCollection, UserCreation, CarCollection, CarDetails, GpsCollection, NewCarCollection, NewOrganizationCollection
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login', obtain_auth_token),
    path('register', UserCreation.as_view()),
    path('cars', CarCollection.as_view()),
    path('cars/<int:pk>/', CarDetails.as_view()),
    path('cars/<int:pk>/gps', GpsCollection.as_view()),
    path('newcars', NewCarCollection.as_view()),
    path('neworg', NewOrganizationCollection.as_view()),
    path('newprofile', NewProfileCollection.as_view())
]
