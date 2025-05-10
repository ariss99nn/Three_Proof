from rest_framework import serializers
from .models import Harvest, Harvest_type, Report_Harvest

class Harvest_Serializer(serializers.Serializer):#creamos el serilizador de cosecha
    class Meta:#clase para mostrar los datos
        model = Harvest#seleccionamos el modelo de cosecha
        fields = '__all__'#los campos que se van a mostrar(ALL SE REIERE A TODOS LOS CAMPOS)
        
class Harvest_type_Serializer(serializers.Serializer):
    class Meta:#clase para mostrar los datos
        model = Harvest_type#seleccionamos el modelo de tipo cosecha
        fields = 'all'#los campos que se van a mostrar(ALL SE REIERE A TODOS LOS CAMPOS)
        
class Report_Harvest_Serializer(serializers.Serializer):
    class Meta:#clase para mostrar los datos
        model = Report_Harvest#seleccionamos el modelo de reporte de cosecha
        fields = '__all__'#los campos que se van a mostrar(ALL SE REIERE A TODOS LOS CAMPOS)