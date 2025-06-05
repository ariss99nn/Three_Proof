from rest_framework import serializers
from .models import Alerta

class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = ['id_alerta', 'seccion', 'tipo_alerta', 'mensaje', 'fecha_hora', 'nivel_criticidad']