from rest_framework import serializers
from .models import Investment


class Investment_Serializer(serializers.Serializer):
    class Meta:
        model = Investment
        fields = '__all__'