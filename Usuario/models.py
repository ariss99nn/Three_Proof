from django.contrib.auth.models import AbstractUser
from django.db import models

# Modelo que extiende al usuario base de Django, añadiendo campos personalizados.
class User(AbstractUser):
    first_name = models.CharField(max_length=100)  # Nombre del usuario
    last_name = models.CharField(max_length=100)   # Apellido del usuario
    document = models.CharField(max_length=20, unique=True)  # Documento de identidad (único)
    phone = models.CharField(max_length=15)        # Número de teléfono
    city = models.CharField(max_length=100)        # Ciudad de residencia
    role = models.CharField(                      # Rol dentro del sistema
        max_length=20,
        choices=[('ADMIN', 'Administrator'), ('AGRICULTOR', 'Farmer')]
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación del registro