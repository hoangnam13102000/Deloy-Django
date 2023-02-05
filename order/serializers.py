from rest_framework import serializers
from . models import Order

class  OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Order
        fields = (
            'id','customer','customer_name','product', 'total_price','quantity' ,'shipping_address','phone_number', 'payment_method','created_at','status'
        )
