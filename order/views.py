from django.shortcuts import render ####
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
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailView(generics.GenericAPIView):
    serializer_class = serializers.OrderSerializers
    permission_classes = [IsAdminUser,]
    def get(self,request,pk):
        order = Orders.objects.get(id=pk)
        serializers = self.serializer_class(order)
        return Response(seriliazers.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        order = Orders.objects.get(id=pk)
        serializers = self.serializer_class(data=request.data,instance=order)
        if serializers.is_valid():
            seriliazers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        order = Orders.objects.get(id=pk)
        order.delete()
        return Response(status=status.HTTP_200_OK)

#codebase for updating the status 

class StatusUpdateView(generics.GenericAPIView):
    serializer_class = serializers.StatusSerializers
    permission_classes = [IsAdminUser,]
    def put(self,request,pk):
        order = Orders.objects.get(id=pk)
        serializers = self.serializer_class(data=request.data,instance=order)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

        

