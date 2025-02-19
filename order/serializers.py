from rest_framework import serializers as s
from .models import *




class OrderItemSerializer(s.ModelSerializer):
    class Meta:
        model = OrderItem
        fields=('product','quantity')
    
class OrderSerializer(s.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id','created_at','total_sum','items')
    
    def create(self, validated_data):
        items = validated_data.pop('items')
        validated_data['user'] = self.context['request'].user
        order = super().create(validated_data)
        total_sum = 0
        order_items = []
        for item in items:
           order_items.append(OrderItem(
               order = order,
               quantity = item['quantity'],
               product = item['product']
           ))
           total_sum += item['product'].price * item['quantity']
        OrderItem.objects.bulk_create(order_items)
        order.total_sum = total_sum
        order.save()
        return order