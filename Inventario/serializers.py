from rest_framework import serializers
from .models import Quality, Product, Fumigate, Geographic_Studies

class Quality_Serializer(serializers.Serializer):
    class Meta:
        model = Quality
        fields = '__all__'
        
class Product_Serializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class Fumigate_Serializer(serializers.Serializer):
    class Meta:
        model = Fumigate
        fields = '__all__'
        
class Geographic_Studies_Serializer(serializers.Serializer):
    class Meta:
        model = Geographic_Studies
        fields = '__all__'