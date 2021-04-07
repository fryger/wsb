from django.urls import path
from .views import MapView, CarDetail, GenericAPIView

urlpatterns = [
    path("", MapView.as_view()),
    path("api/car/<int:id>", GenericAPIView.as_view()),
    path("car/<int:id>/", CarDetail.as_view()),

]
