from django.urls import path
from . import views
from .views import ProfileListCreateView, ProfileRetrieveUpdateDestroyView

from rest_framework.routers import DefaultRouter
from django.urls import path, include  # استيراد include



 
urlpatterns = [
    path('register/', views.register,name='register'), 
    path('userinfo/', views.current_user,name='user_info'), 
    path('profiles/', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroyView.as_view(), name='profile-detail'),
     
]