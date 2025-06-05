# Importa viewsets de Django REST Framework
from rest_framework import viewsets

# Importa los modelos de la aplicación
from .models import (
    zona_riego, sensor, configuracion_riego, 
    lectura_sensor, historial_riego, mantenimiento
)
# Importa los serializadores de la aplicación
from .serializers import (
    zona_riegoSerializer, sensorSerializer, 
    configuracion_riegoSerializer, lectura_sensorSeriaizer, 
    historial_riegoSerializer, mantenimientoSerializer
)

# ViewSet para el modelo zona_riego
class zona_riegoViewSet(viewsets.ModelViewSet):
    queryset = zona_riego.objects.all()  # Consulta todas las zonas de riego
    serializer_class = zona_riegoSerializer  # Serializador para el modelo zona_riego
    http_method_names = ['get', 'post', 'put', 'delete']  # Métodos HTTP permitidos

# ViewSet para el modelo sensor
class sensorViewSet(viewsets.ModelViewSet):
    queryset = sensor.objects.all()  # Consulta todos los registros de sensores
    serializer_class = sensorSerializer  # Serializador para el modelo sensor
    http_method_names = ['get', 'post', 'put', 'delete']  # Métodos HTTP permitidos

# ViewSet para el modelo configuracion_riego
class configuracion_riegoViewSet(viewsets.ModelViewSet):
    queryset = configuracion_riego.objects.all()  # Consulta todas las configuraciones de riego
    serializer_class = configuracion_riegoSerializer  # Serializador para el modelo configuracion_riego
    http_method_names = ['get', 'post', 'put', 'delete']  # Métodos HTTP permitidos

# ViewSet para el modelo lectura_sensor
class lectura_sensorViewSet(viewsets.ModelViewSet):
    queryset = lectura_sensor.objects.all()  # Consulta todas las lecturas de sensores
    serializer_class = lectura_sensorSeriaizer  # Serializador para el modelo lectura_sensor
    http_method_names = ['get', 'post']  # Métodos HTTP permitidos

# ViewSet para el modelo historial_riego
class historial_riegoViewSet(viewsets.ModelViewSet):
    queryset = historial_riego.objects.all()  # Consulta todos los historiales de riego
    serializer_class = historial_riegoSerializer  # Serializador para el modelo historial_riego
    http_method_names = ['get']  # Métodos HTTP permitidos

# ViewSet para el modelo mantenimiento
class mantenimientoViewSet(viewsets.ModelViewSet):
    queryset = mantenimiento.objects.all()  # Consulta todos los mantenimientos
    serializer_class = mantenimientoSerializer  # Serializador para el modelo mantenimiento
    http_method_names = ['get', 'post', 'put', 'delete']  # Métodos HTTP permitidos