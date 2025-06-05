from rest_framework import generics
from .models import Alerta
from .serializers import AlertaSerializer

class AlertaListCreateView(generics.ListCreateAPIView):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer

class AlertaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer
    lookup_field = 'id_alerta'

# Create your views here.