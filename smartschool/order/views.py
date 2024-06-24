from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Order, OrderItem
from .serializers import OrderSerializer

class CreateOrderView(APIView):

    def post(self, request, *args, **kwargs):
        user = request.user  # Assuming user is authenticated
        
        # Extract phone_number and city from request data
        phone_number = request.data.get('phone_number')
        city = request.data.get('city')
        
        # Check if phone_number and city are provided
        if not phone_number or not city:
            return Response({"error": "Phone number and city are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create Order instance
        order_data = {
            "city": city,
            "academic_year": request.data.get('academic_year', ''),
            "country": request.data.get('country', ''),
            "phone_number": phone_number,
            "user": user.id if user else None  # User can be None if not authenticated
        }
        
        serializer = OrderSerializer(data=order_data)
        
        if serializer.is_valid():
            order = serializer.save()
            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Add to your urls.py
from django.urls import path
from .views import CreateOrderView

urlpatterns = [
    path('create-order/', CreateOrderView.as_view(), name='create-order'),
]
