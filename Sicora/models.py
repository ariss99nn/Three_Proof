# Importa la clase base Model de Django para crear modelos de base de datos
from django.db import models

# Modelo de zona de riego
class zona_riego(models.Model):
    # Campos de la zona de riego
    nombre_zona = models.CharField(max_length=50)  # Nombre de la zona
    tipo_planta = models.CharField(max_length=50)  # Tipo de planta cultivada
    necesidades_hidricas = models.CharField(max_length=100)  # Necesidades de agua
    exposicion_solar = models.CharField(max_length=50)  # Nivel de exposición al sol

    def __str__(self):
        # Retorna el nombre de la zona
        return self.nombre_zona

# Modelo de sensor
class sensor(models.Model):
    # Campos del sensor
    tipo = models.CharField(max_length=50)  # Tipo de sensor
    estado = models.BooleanField()  # Estado del sensor (activo/inactivo)

    def __str__(self):
        # Retorna el tipo de sensor
        return self.tipo

# Modelo de configuración de riego
class configuracion_riego(models.Model):
    # Campos de configuración
    frecuencia = models.TimeField()  # Frecuencia de riego
    hora_inicio = models.TimeField()  # Hora de inicio del riego
    duracion = models.TimeField()  # Duración del riego
    tipo_riego = models.CharField(max_length=50)  # Tipo de riego (goteo, aspersión, etc.)
    caudal = models.FloatField()  # Caudal de agua (litros/segundo)
    presion = models.FloatField()  # Presión de agua (bar)

    def __str__(self):
        # Retorna la frecuencia de riego
        return self.frecuencia

# Modelo de lectura de sensor
class lectura_sensor(models.Model):
    # Campos de lectura
    fecha_hora = models.DateField()  # Fecha y hora de la lectura
    valor = models.FloatField()  # Valor registrado por el sensor

    def __str__(self):
        # Retorna el valor de la lectura
        return self.valor

# Modelo de historial de riego
class historial_riego(models.Model):
    # Campos del historial
    fecha = models.DateField()  # Fecha del riego
    duracion = models.TimeField()  # Duración del riego
    cantidad_agua = models.FloatField()  # Cantidad de agua utilizada (litros)

    def __str__(self):
        # Retorna la duración del riego
        return self.duracion

# Modelo de mantenimiento
class mantenimiento(models.Model):
    # Campos de mantenimiento
    fecha = models.DateField()  # Fecha de mantenimiento
    descripcion = models.CharField(max_length=200)  # Descripción de la actividad
    tipo = models.CharField(max_length=50)  # Tipo de mantenimiento

    def __str__(self):
        # Retorna la descripción del mantenimiento
        return self.descripcion
# fin del archivo sistema/models.py