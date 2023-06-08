from django.shortcuts import render
from rest_framework import generics, status 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from . import serializers
from .models import Orders

# Create your views here.


class OrderView(generics.GenericAPIView):
    serializer_class = serializers.OrderSerializers
    queryset = Orders.objects.all()
    def get(self,request):
        order = Orders.objects.all()
        serializers = self.serializer_class(order,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)



    def post(self,request):

        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.lsave()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

