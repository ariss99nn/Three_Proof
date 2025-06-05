from django.urls import path
from .views import InvernaderoListCreateView, InvernaderoRetrieveUpdateDestroyView

urlpatterns = [
    path('', InvernaderoListCreateView.as_view(), name='invernaderos-list-create'),
    path('<int:id_invernadero>/', InvernaderoRetrieveUpdateDestroyView.as_view(), name='invernaderos-detail'),
]