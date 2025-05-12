from django.db import models

# Create your models here.
class Clasificacion(models.Model):
    variedad = models.CharField(max_length=100)
    clasificacion = models.CharField(max_length=100)
    detalles = models.TextField()
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
class Harvest_type(models.Model):#modelo de tipo de cosecha
    name = models.CharField(max_length=20) #nombre del tipo de cosecha
    start_date = models.DateField#fecha de inicio de la cosecha
    end_date = models.DateField#fecha de finalizacion de la cosecha(AUTOMATIZADO)
    clasification = models.ForeignKey(Clasificacion, on_delete=models.CASCADE)#clasificacion de la cosecha(IMPORTADO DESDE PRODUCTO.CLASIFICACION)
    season = models.CharField(max_length=20, default= "2025 A")
    created_at = models.DateTimeField(auto_now_add= True)
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