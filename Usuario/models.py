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
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="usuario_set",  # Cambia esto
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="usuario_set",  # Cambia esto
        related_query_name="user",
    )

    def __str__(self):
        return self.username
