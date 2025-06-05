from django.urls import path
from .views import ConfiguracionListCreateView, ConfiguracionRetrieveUpdateDestroyView

urlpatterns = [
    path('', ConfiguracionListCreateView.as_view(), name='configuraciones-list-create'),
    path('<int:id_config>/', ConfiguracionRetrieveUpdateDestroyView.as_view(), name='configuraciones-detail'),
]