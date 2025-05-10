from django.db import models

# Create your models here.
class Monitoring(models.Model):#crreamos modelo de seguimiento de cultivo
    name = models.CharField(max_length=20)#nombre de cultivo(RELACIONAL A EL NOMBRE DE LA SIEMBRA)
    description = models.TextField#descripcion de evento durante el cultivo
    date = models.DateTimeField#fecha estimada de el suceso
    response = models.TextField#respuesta o recomendacion
    
    def __str__(self):
        return self.name
    

class Prediction(models.Model):#modelo de prediccion
    date = models.DateTimeField
    value =  models.DecimalField
    stock_exchange = models.DecimalField
    
    
class Investment(models.Model):#imodelo de inversion
    value = models.DecimalField
    date = models.DateTimeField
    reason = models.TextField
    