from django.db import models
from Secciones_inv.models import SeccionCultivo  # Importamos la sección

class Sensor(models.Model):
    id_sensor = models.AutoField(primary_key=True)              # ID único
    tipo_sensor = models.CharField(max_length=50)               # Tipo de sensor (ej: humedad)
    unidad_medida = models.CharField(max_length=20)             # Unidad (ej: %, lux)
    seccion = models.ForeignKey(SeccionCultivo, on_delete=models.CASCADE)  # Relación con sección
    estado = models.CharField(max_length=20)                    # Estado: activo, inactivo
    intervalo_med = models.IntegerField()                       # Intervalo en minutos

    def __str__(self):
        return f"{self.tipo_sensor} - {self.seccion.nombre_seccion}"