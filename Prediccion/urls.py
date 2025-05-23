from django.urls import path
from .views import PredictionListCreateAPIView, PredictionRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('predictions/', PredictionListCreateAPIView.as_view(), name='prediction-list-create'),
    path('predictions/<int:pk>/', PredictionRetrieveUpdateDestroyAPIView.as_view(), name='prediction-detail'),
]
# This code defines the URL patterns for the Prediction API, allowing for listing, creating, retrieving, updating, and deleting predictions.