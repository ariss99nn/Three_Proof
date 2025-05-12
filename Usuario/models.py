from django.db import models
from django.contrib.auth.models import AbstractUser
import pandas as  pd

# Create your models here.
class User(AbstractUser):
    
    Rol_Choices = (
        ('ADMIN', 'Administrator'),
        ('FARM','Farmer'),
    )
    
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    document = models.CharField(max_length=10, unique= True)
    contact = models.CharField(max_length= 10)
    email =  models.EmailField
    role = models.CharField(max_length=20,choices=Rol_Choices)
    ubication =  models.CharField
    created_at = models.DateTimeField(auto_now_add= True)