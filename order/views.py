from django.shortcuts import render
from rest_framework import generics, status 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from . import serializers
from .models import Orders

# Create your views here.


class OrderView(generics.GenericAPIView):
    serializer_class = Orders.OrderSerializers
    queryset = Orders.objects.all()
    def get(self,request):
        pass


    def post(self,request):
        pass
