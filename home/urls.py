from django.urls import path, include
from .views import CarView, CarDetail, GpsView

urlpatterns = [
    path('cars/', CarView.as_view()),
    path('cars/<int:id>/', CarDetail.as_view()),
    path('cars/<int:id>/gps/', GpsView.as_view()),
    # path("", MapView.as_view()),
    # path("api/car/<int:id>", GenericAPIView.as_view()),
    # path("car/<int:id>/", CarDetail.as_view()),

]
