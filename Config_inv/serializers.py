from rest_framework import serializers
from .models import ConfiguracionCultivo

class ConfiguracionCultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfiguracionCultivo
        fields = ['id_config', 'tipo_cultivo', 'parametro', 'valor_minimo', 'valor_maximo', 'unidad']