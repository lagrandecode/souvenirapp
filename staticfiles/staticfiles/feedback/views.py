from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import status, generics 
from . import serializers
from .models import Feedback


# Create your views here.

class FeedbackView(generics.GenericAPIView):
    serializer_class = serializers.FeedbackSerializer
    queryset = Feedback.objects.all()
    def get(self,request):
        feedback = Feedback.objects.all()
        serilializers = self.serializer_class(feedback,many=True)
        return Response(serilializers.data,status=status.HTTP_200_OK)
    def post(self,request):
        data = request.data
        serializers = self.serializer_class(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(seriliazers.errors,status=status.HTTP_400_BAD_REQUEST)

        