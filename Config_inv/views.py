from rest_framework import generics
from .models import ConfiguracionCultivo
from .serializers import ConfiguracionCultivoSerializer

# Lista todas las configuraciones y permite crear nuevas
class ConfiguracionListCreateView(generics.ListCreateAPIView):
    queryset = ConfiguracionCultivo.objects.all()
    serializer_class = ConfiguracionCultivoSerializer

# Ver, editar o eliminar una configuración por ID
class ConfiguracionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConfiguracionCultivo.objects.all()
    serializer_class = ConfiguracionCultivoSerializer
    lookup_field = 'id_config'