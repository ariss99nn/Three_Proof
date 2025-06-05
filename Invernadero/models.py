from django.db import models
from Usuario.models import User  # Importamos el modelo Usuario para la relación

# Creamos la clase Invernadero como tabla de base de datos
class Invernadero(models.Model):
    id_invernadero = models.AutoField(primary_key=True)  # ID autoincremental
    nombre = models.CharField(max_length=100)            # Nombre del invernadero
    ubicacion = models.CharField(max_length=200)         # Ubicación o dirección
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con Usuario
    fecha_creacion = models.DateTimeField(auto_now_add=True)        # Fecha automática

    def __str__(self):
        return f"{self.nombre} - {self.ubicacion}"


# Create your models here.