from rest_framework import generics
from .models import ActuadorRiego
from .serializers import ActuadorRiegoSerializer

# Listar y crear actuadores
class ActuadorListCreateView(generics.ListCreateAPIView):
    queryset = ActuadorRiego.objects.all()
    serializer_class = ActuadorRiegoSerializer

# Ver, editar o eliminar un actuador por ID
class ActuadorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActuadorRiego.objects.all()
    serializer_class = ActuadorRiegoSerializer
    lookup_field = 'id_actuador'