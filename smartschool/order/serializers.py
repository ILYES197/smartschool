from rest_framework import serializers
from .models import Order,OrderItem


class OrderItemsSerializer(serializers.ModelSerializer):
    formation_link = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem  # افترض أن هذا هو النموذج المرتبط بـ OrderItem
        fields = "__all__"  # يتضمن جميع الحقول بالإضافة إلى الحقل الجديد

    def get_formation_link(self, obj):
        if obj.formation:
            return obj.formation.link
        return None

        
        
class OrderSerializer(serializers.ModelSerializer):
    orderItems = serializers.SerializerMethodField(method_name="get_order_items", read_only=True)
    
    class Meta:
        model = Order
        fields = "__all__"
        
    def get_order_items(self, obj):
        order_items = obj.orderitems.all()  # تأكد أن العلاقة صحيحة بين Order و OrderItems
        serializer = OrderItemsSerializer(order_items, many=True)
        return serializer.data
