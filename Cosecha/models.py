from django.db import models

# Create your models here.
class Harvest_type(models.Model):#modelo de tipo de cosecha
    name = models.CharField(max_length=20) #nombre del tipo de cosecha
    start_date = models.DateTimeField#fecha de inicio de la cosecha
    end_date = models.DateTimeField#fecha de finalizacion de la cosecha(AUTOMATIZADO)
    clasification = models.CharField(max_length=20)#clasificacion de la cosecha(IMPORTADO DESDE PRODUCTO.CLASIFICACION)
    def __str__(self):
        return self.name#manera en que se muestra el modelo en este caso NOMBRE
    
class Harvest(models.Model):#modelo de cosecha
    name = models.CharField(max_length=20)#nombre de la cosecha
    amount = models.IntegerField#cantidad recolectada de la cosecha
    harvest_form = models.BooleanField#forma de recolecccion de la cosecha(MANUAL O MECANIZADA)
    type = models.ForeignKey(Harvest_type, on_delete=models.CASCADE)#tipo de cosecha(RELACIONAL A MODELO DE TIPO DE COSECHA)
    
    def __str__(self):
        return self.name

class Report_Harvest(models.Model):#modelo de reporte de la cosecha
    name = models.ForeignKey(Harvest, on_delete=models.CASCADE)#nombre del reporte
    clasification = models.CharField(max_length=30)#clasificacion de producto relacionada a (CLASIFICACION DE COSECHA)
    price = models.DecimalField(decimal_places=2)#precio por el que se podria vender la cosecha
    quality = models.CharField#calidad de producto(RELACIONAL A CALIDAD DE PRODUCTO )
    diagram = models.IntegerField#datos que se almacenan para mostrar en una grafica
    
    def __str__(self):
        return self.name