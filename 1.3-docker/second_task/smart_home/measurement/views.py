# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework import generics
from .models import Sensor, TemperatureMeasurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementCreateSerializer


class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class TemperatureMeasurementCreateView(generics.CreateAPIView):
    queryset = TemperatureMeasurement.objects.all()
    serializer_class = MeasurementCreateSerializer



