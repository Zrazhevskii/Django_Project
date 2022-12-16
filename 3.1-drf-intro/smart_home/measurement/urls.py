from django.urls import path

from .views import SensorAPIView, SensorIdView, SensorDetail, MeasurementAPIView

urlpatterns = [
    path('sensor/', SensorAPIView.as_view()),
    path('sensor/upload/<pk>/', SensorIdView.as_view()),
    path('sensor/details/<pk>/', SensorDetail.as_view()),
    path('measurement/', MeasurementAPIView.as_view()),
]
