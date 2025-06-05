from django.urls import path
from .views import SeccionListCreateView, SeccionRetrieveUpdateDestroyView

urlpatterns = [
    path('', SeccionListCreateView.as_view(), name='secciones-list-create'),  # /api/secciones/
    path('<int:id_seccion>/', SeccionRetrieveUpdateDestroyView.as_view(), name='secciones-detail'),  # /api/secciones/1/
]