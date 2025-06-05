from django.db import models

class ConfiguracionCultivo(models.Model):
    id_config = models.AutoField(primary_key=True)                 # ID único
    tipo_cultivo = models.CharField(max_length=50)                 # Ej: lechuga, tomate
    parametro = models.CharField(max_length=50)                    # Ej: humedad_min, luz_max
    valor_minimo = models.DecimalField(max_digits=5, decimal_places=2)  # Ej: 30.00
    valor_maximo = models.DecimalField(max_digits=5, decimal_places=2)  # Ej: 60.00
    unidad = models.CharField(max_length=10)                       # Ej: %, ppm

    def __str__(self):
        return f"{self.tipo_cultivo} - {self.parametro}"