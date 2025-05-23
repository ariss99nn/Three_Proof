from django.shortcuts import render
from django.views import APIview
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Harvest, Harvest_Details, Harvest_Type, Classification
from .serializers import Harvest_Serializer, HarvestDeatils_Serializers, Harvest_type_Serializer, Classification_Serializer
from django.shortcuts import get_object_or_404

# Create your views here
class Harvest_List_View(APIview):
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
    
    
    
class Harvest_Details_view(APIview):
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
    
class Classification_List_view(APIview):
        def get(self, request):
            classification = Classification.objects.all()
            serializer = Classification_Serializer(classification, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        def post(self, request):
            serializer = Classification_Serializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class Classification_Details_View(APIview):
    """
    Retrieve, update or delete a Classification instance.
    """
    def get_object(self, pk):
        try:
            return Classification.objects.get(pk=pk)
        except Classification.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        classification = self.get_object(pk)
        serializer = Classification_Serializer(classification)
        return Response(serializer.data)

    def put(self, request, pk):
        classification = self.get_object(pk)
        serializer = Classification_Serializer(classification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        classification = self.get_object(pk)
        classification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Harvest_Type_List(APIview):
    """
    List all Harvest Types, or create a new Harvest Type.
    """
    def get(self, request):
        harvest_type = Harvest_Type.objects.all()
        serializer = Harvest_type_Serializer(harvest_type, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Harvest_type_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Harvest_Type_Details_List(APIview):
    """
    Retrieve, update or delete a Harvest Type instance.
    """
    def get_object(self, pk):
        try:
            return Harvest_Type.objects.get(pk=pk)
        except Harvest_Type.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        harvest_type = self.get_object(pk)
        serializer = Harvest_type_Serializer(harvest_type)
        return Response(serializer.data)

    def put(self, request, pk):
        harvest_type = self.get_object(pk)
        serializer = Harvest_type_Serializer(harvest_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        harvest_type = self.get_object(pk)
        harvest_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Harvest_Details_List(APIview):
    """
    List all Harvest Details, or create new Harvest Details.
    """
    def get(self, request):
        harvest_details = Harvest_Details.objects.all()
        serializer = HarvestDeatils_Serializers(harvest_details, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HarvestDeatils_Serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Harvest_Details_Detail_List(APIview):
    """
    Retrieve, update or delete Harvest Details instance.
    """
    def get_object(self, pk):
        try:
            return Harvest_Details.objects.get(pk=pk)
        except Harvest_Details.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        harvest_details = self.get_object(pk)
        serializer = HarvestDeatils_Serializers(harvest_details)
        return Response(serializer.data)

    def put(self, request, pk):
        harvest_details = self.get_object(pk)
        serializer = HarvestDeatils_Serializers(harvest_details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        harvest_details = self.get_object(pk)
        harvest_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   