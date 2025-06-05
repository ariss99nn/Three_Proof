from django.urls import path
from .views import LecturaListCreateView, LecturaRetrieveUpdateDestroyView

urlpatterns = [
    path('', LecturaListCreateView.as_view(), name='lecturas-list-create'),
    path('<int:id_lectura>/', LecturaRetrieveUpdateDestroyView.as_view(), name='lecturas-detail'),
]