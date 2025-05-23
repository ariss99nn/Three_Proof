from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import predictionView

router= DefaultRouter()

router.register(r'Prediction', predictionView, basename='Prediction')

urlpatterns = [
    path('', include(router.urls)),
]


