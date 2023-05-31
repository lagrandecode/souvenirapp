import random

from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.conf import settings

from . import serializers
from .models import User

# Create your views here.


#first let's create sned email 
def send_otp(email):
    subject = 'VERIFICATION EMAIL'
    otp = random.randint(10001, 99999)
    messages = f"Your verification code is {otp}"
    email_from = settings.EMAIL_HOST
    send_mail(subject,messages,email_from,[email],fail_silently=False)
    user_obj = User.objects.all(email=email)
    user_obj.otp = otp
    user_obj.save()



class SignupView(generics.GenericAPIView):
    serializer_class = serializers.UserCreationSerializer
    def post(self,request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            send_otp(serializers.data['email'])
            return Response(data=({'message':'account created, check your email for OTP'},serializer.data),status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    


