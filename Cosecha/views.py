from django.shortcuts import render
from django.views import Apiview
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Harvest, Harvest_Details, Harvest_Type, Classification
from .serializers import Harvest_Serializer, HarvestDeatils_Serializers, Harvest_type_Serializer, Classification_Serializer
from django.shortcuts import get_object_or_404

# Create your views here.
class Harvest_List_View(Apiview):
    def get(self, request):
        harvests = Harvest.objects.all()
        serializer = Harvest_Serializer(harvests, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = Harvest_Serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Harvest_Details_view(Apiview):
    def get(self,pk):
        try:
           return Harvest.objects.get(pk = pk)
        except Harvest.DoesNotExist:
            raise Http404("Harvest not found")
        
    def get(self, request, pk):
        harvest = self.get_object(pk)
        serializer = Harvest_Serializer(harvest)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, pk):
        harvest = self.get_object(pk)
        serializer =Harvest_Serializer(harvest, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        harvest = self.get_object(pk)
        harvest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    