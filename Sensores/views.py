from rest_framework import generics
from .serializers import sensorserializer
from .models import Sensor

class sensorList (generics.ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = sensorserializer

class sensorCreate (generics.CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = sensorserializer

class  sensorRetrieve (generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = sensorserializer

class sensorUpdate (generics.UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = sensorserializer

class sensorDestroy (generics.DestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = sensorserializer

