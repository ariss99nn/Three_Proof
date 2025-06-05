from django.db import models

# Análisis químico del suelo antes o durante el cultivo.
class SoilAnalysis(models.Model):
    ph = models.FloatField()                 # Nivel de pH
    salinity = models.FloatField()           # Nivel de salinidad
    nitrogen = models.FloatField()           # Contenido de nitrógeno
    phosphorus = models.FloatField()         # Contenido de fósforo
    potassium = models.FloatField()          # Contenido de potasio
    humidity = models.FloatField()           # Humedad del suelo
    results = models.TextField()             # Resultados detallados
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)  # Coordenadas
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    date = models.DateField()                # Fecha del análisis
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    
    
# class Terrain(models.Model):
#     type = models.CharField(max_length=100)  # Tipo de terreno
#     description = models.CharField(max_length=100)  # Descripción del terreno
#     property = models.CharField(max_length=100)  # Propiedad del terreno
#     location = models.CharField(max_length=100)  # Ubicación del terreno
#     created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
#      # Propietario del terreno
    