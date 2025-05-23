from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Product_List_View

router= DefaultRouter()

router.register(r'Product', Product_List_View ,basename='Product')

urlpatterns = [
    path('', include(router.urls)),
]


