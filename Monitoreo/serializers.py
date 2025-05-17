from rest_framework import serializers
from .models import CropMonitoring

class CropMonitoring_Serializer(serializers.Serializer):
    class Meta:
        model = CropMonitoring
        fields = '__all__'