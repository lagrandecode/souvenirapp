
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from . import serializers
from .models import Orders


class OrderView(generics.GenericAPIView):
    serializer_class = serializers.OrderSerializers

    def get_queryset(self):
        return Orders.objects.all()

    def get(self, request):
        orders = self.get_queryset()
        serialized_data = self.serializer_class(orders, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request):
        # permission_classes = [IsAdminUser]
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(generics.GenericAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = serializers.OrderSerializers

    def get_queryset(self):
        return Orders.objects.all()

    def get(self, request, pk):
        order = self.get_queryset().get(id=pk)
        serializer = self.serializer_class(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        order = self.get_queryset().get(id=pk)
        serializer = self.serializer_class(data=request.data, instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = self.get_queryset().get(id=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StatusUpdateView(generics.GenericAPIView):
    serializer_class = serializers.StatusSerializers
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Orders.objects.all()

    def put(self, request, pk):
        order = self.get_queryset().get(id=pk)
        serializer = self.serializer_class(data=request.data, instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
