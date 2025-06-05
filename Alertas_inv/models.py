from django.db import models
from Secciones_inv.models import SeccionCultivo  # Importamos la sección relacionada

class Alerta(models.Model):
    id_alerta = models.AutoField(primary_key=True)           # ID único
    seccion = models.ForeignKey(SeccionCultivo, on_delete=models.CASCADE)
    tipo_alerta = models.CharField(max_length=50)            # Ej: humedad baja, plaga
    mensaje = models.TextField()                             # Descripción
    fecha_hora = models.DateTimeField(auto_now_add=True)     # Fecha automática
    nivel_criticidad = models.CharField(max_length=20)       # baja, media, alta

    def __str__(self):
        return f"[{self.nivel_criticidad.upper()}] {self.tipo_alerta} - {self.seccion.nombre_seccion}"