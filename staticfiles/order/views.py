

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from . import serializers
from .models import Orders


class OrderView(generics.GenericAPIView):
    serializer_class = serializers.OrderSerializers
    queryset = Orders.objects.all()

    def get(self, request):
        order = Orders.objects.all()
        serializer = self.serializer_class(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(generics.GenericAPIView):
    queryset = Orders.objects.all()
    serializer_class = serializers.OrderSerializers
    permission_classes = [IsAdminUser,]

    def get(self, request, pk):
        order = Orders.objects.get(id=pk)
        serializer = self.serializer_class(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        order = Orders.objects.get(id=pk)
        serializer = self.serializer_class(data=request.data, instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = Orders.objects.get(id=pk)
        order.delete()
        return Response(status=status.HTTP_200_OK)


class StatusUpdateView(generics.GenericAPIView):
    queryset = Orders.objects.all()
    serializer_class = serializers.StatusSerializers
    permission_classes = [IsAdminUser,]

    def put(self, request, pk):
        order = Orders.objects.get(id=pk)
        serializer = self.serializer_class(data=request.data, instance=order)
        serializer.is_valid(raise_exception=True)  # Validate the serializer
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
   

