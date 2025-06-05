from django.db import models
from Sensor_inv.models import Sensor  # Importamos la relación

class LecturaSensor(models.Model):
    id_lectura = models.AutoField(primary_key=True)                  # ID único
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)     # Sensor relacionado
    valor = models.DecimalField(max_digits=6, decimal_places=2)      # Valor como 28.75
    fecha_hora = models.DateTimeField(auto_now_add=True)             # Se genera automáticamente

    def __str__(self):
        return f"{self.sensor.tipo_sensor} - {self.valor} @ {self.fecha_hora}"


# Create your models here.