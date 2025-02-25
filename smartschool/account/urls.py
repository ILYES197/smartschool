from django.urls import path
from . import views
from .views import حساب_تجاري_ViewSet


urlpatterns = [
    path('register/', views.register,name='register'), 
    path('userinfo/', views.current_user,name='user_info'), 
    path('حساب_تجاري/', حساب_تجاري_ViewSet.as_view({'get': 'list', 'post': 'create'}), name='حساب_تجاري-قائمة'),
    path('حساب_تجاري/<int:pk>/', حساب_تجاري_ViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='حساب_تجاري-تفاصيل'),

]