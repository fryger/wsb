from home.models import User
from django.urls import path, re_path, include
#from .views import NewProfileCollection, UserCreation, CarCollection, CarDetails, GpsCollection, NewCarCollection, NewOrganizationCollection
from .views import UserCreation, OrganizationCollection, UserDetail, DriverCollection, DriverDetail, UpdateDriverPassword, CarCollection, CarDetail, GpsCollection, GpsPointCreation, MaintenanceCollection, MaintenanceDetails, MyFileView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('token', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('login', obtain_auth_token),
    path('register', UserCreation.as_view()),
    path('organization', OrganizationCollection.as_view()),
    path('profile', UserDetail.as_view()),
    path('drivers', DriverCollection.as_view()),
    path('drivers/<int:pk>/', DriverDetail.as_view()),
    path('drivers/<int:pk>/changepassword', UpdateDriverPassword.as_view()),
    path('cars', CarCollection.as_view()),
    path('cars/location', GpsPointCreation.as_view()),
    path('cars/<int:pk>/maintenance', MaintenanceCollection.as_view()),
    path('cars/<int:pk>/maintenance/<int:pk2>', MaintenanceDetails.as_view()),
    path('cars/<int:pk>/', CarDetail.as_view()),
    path('cars/<int:pk>/gps', GpsCollection.as_view()),
    path('upload', MyFileView.as_view())
]
