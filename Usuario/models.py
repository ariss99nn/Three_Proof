from django.db import models
import pandas as  pd

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    document = models.IntegerField
    contact = models.IntegerField
    email =  models.EmailField
    role = models.CharField
    ubication =  models.CharField