from django.urls import path
from .views import SensorListCreateView, SensorRetrieveUpdateDestroyView

urlpatterns = [
    path('', SensorListCreateView.as_view(), name='sensores-list-create'),
    path('<int:id_sensor>/', SensorRetrieveUpdateDestroyView.as_view(), name='sensores-detail'),
]