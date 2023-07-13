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
    try:
        user_obj = User.objects.get(email=email)
        user_obj.otp = otp
        user_obj.save()
    except User.DoesNotExist:
        user_obj = User(email=email,otp=otp)
        user_obj.save()
    send_mail(subject,messages,email_from,[email],fail_silently=False)

#codebase for sign in 
class SignupView(generics.GenericAPIView):
    serializer_class = serializers.UserCreationSerializer
    def post(self,request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            send_otp(serializers.data['email'])
            return Response(data=({'message':'account created, check your email for OTP'},serializers.data),status=status.HTTP_201_CREATED)
        return Response(data=serializers.errors,status=status.HTTP_400_BAD_REQUEST)
  
#codebase for verifying OTP
class VerifyView(generics.GenericAPIView):
    serializer_class = serializers.VerifySerializer
    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                user = User.objects.filter(email=email)
                if not user.exists():
                    return Response({'message':'Something went wrong','data':'wrong email'},status=status.HTTP_400_BAD_REQUEST)
                if user[0].otp !=otp:
                    return Response({'message':'Something went wrong','data':'wrong otp'},status=status.HTTP_400_BAD_REQUEST)
                user = user.first()
                user.isVerified == True
                user.save()
                return Response({
                    'message':'account verified',
                    'data':{}
                },status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)


#admin login 

class AdminLogin(generics.GenericAPIView):
    def get(self,request):
        if request.user.is_authenticated:
            return Response({'message':'Home page'},status=status.HTTP_200_OK)
        return Response({'message':'admin'},status=status.HTTP_200_OK)