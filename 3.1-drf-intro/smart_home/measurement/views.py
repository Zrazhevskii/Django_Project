# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.http import HttpResponse
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, RetrieveAPIView, CreateAPIView, \
    ListCreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer


def home(request):
    return HttpResponse('<h1>Супер клевый сайт...  в будущем</h1>')


""" Получение данных по датчикам """

class SensorView(APIView):
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


class SensorUpload(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


    ''' Просмотр всех измерений '''
class MeasurementView(APIView):
    def get(self, request):
        s = Measurement.objects.all()
        return Response({'measurements': MeasurementSerializer(s, many=True).data})

    """Добовляем измерение датчику. Указываются ID датчика и температура."""
    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'measurement': serializer.data})

''' Получить информацию по конкретному датчику. 
    Выдается полная информация по датчику: 
    ID, название, описание и список всех измерений с температурой и временем.'''

class SensorDetail(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
