from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    distance_inter_plants = models.FloatField(help_text= "En metros")
    merchar_price = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_area = models.FloatField(help_text="Relacion planta/m2")
    unity_of_medida = models.CharField(max_length=20, choices= [('Kg', 'Kilogramos'), ('L', 'Litros'), ('m2', 'Metros Cuadrados')])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    

    
    