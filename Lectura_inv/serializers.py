from rest_framework import serializers
from .models import LecturaSensor

class LecturaSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LecturaSensor
        fields = ['id_lectura', 'sensor', 'valor', 'fecha_hora']