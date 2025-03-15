from django.urls import path
from . import views
from .views import CreateOrderView
from .views import UserOrdersView

urlpatterns = [
    path('orders/new/', CreateOrderView.as_view(),name='new_order'), 
  
    

    path('user-orders/', UserOrdersView.as_view(), name='user-orders'),

]