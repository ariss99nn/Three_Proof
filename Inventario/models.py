from django.db import models

# Create your models here.
class Quality(models.Model):#creamos el modelo de calidad
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=20)
    distance = models.TextField
    area = models.IntegerField
    varity = models.TextField
    
    def __str__(self):
        return self.name
    
class Fumigate(models.Model):
    name_product = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=3)#precio predictivo en base a la TAZA DE VALORES
    description = models.TextField
    use_case = models.TextField
    application_method= models.TextField
    
    
class Geographic_Studies(models.Model):
    ph = models.IntegerField
    salinity = models.CharField
    nitro = models.DecimalField
    phosphorus = models.DecimalField
    potassium = models.DecimalField
    result = models.DecimalField
    humidity = models.DecimalField
    study_date = models.DateTimeField