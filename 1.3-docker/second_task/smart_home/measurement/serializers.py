# # TODO: опишите необходимые сериализаторы
from rest_framework import serializers
from .models import Sensor, TemperatureMeasurement


class MeasurementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureMeasurement
        fields = ['sensor', 'temperature', 'created_at']


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementCreateSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

