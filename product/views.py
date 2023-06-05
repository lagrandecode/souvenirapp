from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from .models import Product
from rest_framework.permissions import IsAuthenticated


# Create your views here.



class ProductView(generics.GenericAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    def get(self,request):
        product = Product.objects.all()
        serializer = self.serializer_class(product,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ProductViewDetail(generics.GenericAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        serializers = serializer_class()
        pass

    def put(self,request,pk):
        pass

    def delete(self,request,pk):
        pass
