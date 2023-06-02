from rest_framework import generics,status
from rest_framework.response import Response
from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        