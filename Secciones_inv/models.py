from django.db import models
from Invernadero.models import Invernadero  # Importamos modelo padre

class SeccionCultivo(models.Model):
    id_seccion = models.AutoField(primary_key=True)               # Clave primaria
    nombre_seccion = models.CharField(max_length=100)             # Ej: "Sección A - Tomate"
    invernadero = models.ForeignKey(Invernadero, on_delete=models.CASCADE)  # Relación
    cultivo_actual = models.CharField(max_length=50)              # Cultivo sembrado actualmente

    def __str__(self):
        return f"{self.nombre_seccion} ({self.cultivo_actual})"