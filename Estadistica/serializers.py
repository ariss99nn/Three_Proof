from rest_framework import serializers
from .models import Monitoring

class Monitoring_Serializer(serializers.Serializer):
    class Meta:
        model = Monitoring#seleciionamos el modelo de seguimiento
        fields = '__all__'