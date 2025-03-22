from django.urls import path
from . import views
from .views import CreateOrderView
from .views import UserOrdersView

urlpatterns = [
    path('orders/new/', CreateOrderView.as_view(),name='new_order'), 
<<<<<<< HEAD
  #path('orders/', views.get_orders,name='get_orders'), 
   #path('orders/<str:pk>/', views.get_order,name='get_order'), 
=======
  
>>>>>>> 7cb928f279a365f5e97b4268eb287317d67d7e1e
    

    path('user-orders/', UserOrdersView.as_view(), name='user-orders'),

]