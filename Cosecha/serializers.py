from rest_framework import serializers
from .models import Harvest, Classification, HarvestType, HarvestDetails

class Classification_Serializer(serializers.Serializer):
    class Meta:
        model = Classification
        fields = '__all__'


class Harvest_Serializer(serializers.Serializer):#creamos el serilizador de cosecha
    class Meta:#clase para mostrar los datos
        model = Harvest#seleccionamos el modelo de cosecha
        fields = '__all__'#los campos que se van a mostrar(ALL SE REIERE A TODOS LOS CAMPOS)
        
class Harvest_type_Serializer(serializers.Serializer):
    class Meta:#clase para mostrar los datos
        model = HarvestType#seleccionamos el modelo de tipo cosecha
        fields = 'all'#los campos que se van a mostrar(ALL SE REIERE A TODOS LOS CAMPOS)
        
class HarvestDeatils_Serializers(serializers.Serializer):
    class Meta:
        model=HarvestDetails
        fields = '__all__'