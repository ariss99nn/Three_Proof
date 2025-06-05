from django.urls import path
from .views import AlertaListCreateView, AlertaRetrieveUpdateDestroyView

urlpatterns = [
    path('', AlertaListCreateView.as_view(), name='alertas-list-create'),
    path('<int:id_alerta>/', AlertaRetrieveUpdateDestroyView.as_view(), name='alertas-detail'),
]