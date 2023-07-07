from rest_framework import serializers
from .models import Orders
# from product.serializers import ProductSerializer


class OrderSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Orders
        fields = '__all__'
        depth = 1


class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['status']