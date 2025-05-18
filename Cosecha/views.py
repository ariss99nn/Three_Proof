from django.shortcuts import render
from django.views import Apiview
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Harvest, Harvest_Details, Harvest_Type
from .serializers import Harvest_Serializer, HarvestDeatils_Serializers, Harvest_type_Serializer

# Create your views here.
