from django.urls import path
from .views import (
    UserListCreateAPIView,
    UserRetrieveUpdateDestroyAPIView,
    UserMeAPIView
)


urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('users/me/', UserMeAPIView.as_view(), name='user-me'),
    
]
