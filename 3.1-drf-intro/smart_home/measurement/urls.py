from django.urls import path

from .views import SensorView, SensorUpload, SensorDetail, MeasurementView

urlpatterns = [
    path('sensor/', SensorView.as_view()),
    path('sensor/upload/<pk>/', SensorUpload.as_view()),
    path('sensor/<pk>/', SensorDetail.as_view()),
    path('measurement/', MeasurementView.as_view()),
]
