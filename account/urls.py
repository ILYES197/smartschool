from django.urls import path
from . import views
 

from .views import TransferRequestViewSet
from .views import profile_view
 
urlpatterns = [
    path('register/', views.register,name='register'), 
    path('userinfo/', views.current_user,name='user_info'), 
   
    path('profile/', views.profile_view, name='profile'),

    path('transfer-requests/', TransferRequestViewSet.as_view({'get': 'list', 'post': 'create'}), name='transfer-list'),
    path('transfer-requests/<int:pk>/', TransferRequestViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='transfer-detail'),
]