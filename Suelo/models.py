from django.db import models

# Create your models here.
class Geographic_Studies(models.Model):
    ph = models.IntegerField
    salinity = models.CharField
    nitro = models.DecimalField
    phosphorus = models.DecimalField
    potassium = models.DecimalField
    result = models.DecimalField
    humidity = models.DecimalField
    study_date = models.DateTimeField