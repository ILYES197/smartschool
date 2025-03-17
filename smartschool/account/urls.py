from django.urls import path
from . import views
 

from rest_framework.routers import DefaultRouter
from django.urls import path, include  # استيراد include

from .views import TransferRequestViewSet
from .views import UserProfileView
 
urlpatterns = [
    path('register/', views.register,name='register'), 
    path('userinfo/', views.current_user,name='user_info'), 
    path('profile/', UserProfileView.as_view(), name='user-profile'),  # EndPoint واحد فقط
    path('transfer-requests/', TransferRequestViewSet.as_view({'get': 'list', 'post': 'create'}), name='transfer-list'),
    path('transfer-requests/<int:pk>/', TransferRequestViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='transfer-detail'),
]