from rest_framework import serializers
from .models import Sensor

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id_sensor', 'tipo_sensor', 'unidad_medida', 'seccion', 'estado', 'intervalo_med']