from django.urls import path
from . import views
from .views import ProfileListCreateView, ProfileRetrieveUpdateDestroyView

from rest_framework.routers import DefaultRouter
from django.urls import path, include  # استيراد include

from .views import TransferRequestViewSet


 
urlpatterns = [
    path('register/', views.register,name='register'), 
    path('userinfo/', views.current_user,name='user_info'), 
    path('profiles/', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroyView.as_view(), name='profile-detail'),
    
    path('transfer-requests/', TransferRequestViewSet.as_view({'get': 'list', 'post': 'create'}), name='transfer-list'),
    path('transfer-requests/<int:pk>/', TransferRequestViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='transfer-detail'),
]