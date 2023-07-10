from rest_framework import serializers
from .models import Orders
# from product.serializers import ProductSerializer


class OrderSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Orders
        fields = ['customer','product','email','address','phone_number','order_date','status']
        depth = 1


class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['status']