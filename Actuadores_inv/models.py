from django.db import models
from Secciones_inv.models import SeccionCultivo  # Importamos la relación con sección

class ActuadorRiego(models.Model):
    id_actuador = models.AutoField(primary_key=True)            # ID único
    tipo_actuador = models.CharField(max_length=50)             # Ej: goteo, aspersión
    seccion = models.ForeignKey(SeccionCultivo, on_delete=models.CASCADE)  # Relación
    estado = models.CharField(max_length=20)                    # activo, apagado, automático
    fecha_activacion = models.DateTimeField(auto_now=True)      # Se actualiza automáticamente

    def __str__(self):
        return f"{self.tipo_actuador} ({self.estado})"