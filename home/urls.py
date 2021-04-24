from django.urls import path, include
from .views import CarView, CarDetail, GpsView, UserCreation
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register', UserCreation.as_view()),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
    path('cars/', CarView.as_view()),
    path('cars/<int:id>/', CarDetail.as_view()),
    path('cars/<int:id>/gps/', GpsView.as_view()),
]
