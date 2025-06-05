from rest_framework import serializers
from .models import Sensor
"""Se Modifico el seriallizer por mala 
estrucuturacion segun lineamientos"""
class sensorserializer (serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'