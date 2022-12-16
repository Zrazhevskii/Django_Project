# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer


def home(request):
    return HttpResponse('<h1>Супер клевый сайт...  в будущем</h1>')


class SensorAPIView(APIView):
    """ Получение данных по датчикам """

    def get(self, request):
        s = Sensor.objects.all()
        return Response({'sensors': SensorSerializer(s, many=True).data})

    """ Добавление датчиков """

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'sensor': serializer.data})

    """ Изменение данных датчиков """


class SensorIdView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    """Добавить измерение. Указываются ID датчика и температура"""


class MeasurementAPIView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response({'measurement': serializer.data})


class SensorDetail(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
