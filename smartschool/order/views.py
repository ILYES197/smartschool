from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated ,IsAdminUser
from rest_framework import status
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemsSerializer
from formation.models import formation
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from .models import Order
 

class CreateOrderView(APIView):

    def post(self, request, *args, **kwargs):
        user = request.user  # Assuming user is authenticated
        
        # Extract required fields from request data
        phone_number = request.data.get('phone_number')
        #city = request.data.get('city')
        academic_year = request.data.get('academic_year', '')
       # country = request.data.get('country', '')
        formation_id = request.data.get('formation_id')
        
        # Check if phone_number, city, and formation_id are provided
        if not phone_number or not city or not formation_id:
            return Response({"error": "Phone number, city, and formation_id are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            formation_obj = formation.objects.get(id=formation_id)
        except formation.DoesNotExist:
            return Response({"error": "Formation not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Create Order instance
        order_data = {
            "city": city,
            "academic_year": academic_year,
            "country": country,
            "phone_number": phone_number,
            "user": user.id if user else None  # User can be None if not authenticated
        }
        
        order_serializer = OrderSerializer(data=order_data)
        
        if order_serializer.is_valid():
            order = order_serializer.save()
            
            # Create OrderItem for the formation
            order_item_data = {
                "formation": formation_obj.id,
                "order": order.id,
                "name": formation_obj.name,
                "price": formation_obj.price
            }
            
            order_item_serializer = OrderItemsSerializer(data=order_item_data)
            
            if order_item_serializer.is_valid():
                order_item_serializer.save()
                return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
            else:
                order.delete()  # Rollback order if order item creation fails
                return Response(order_item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)
