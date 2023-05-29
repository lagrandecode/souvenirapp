from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status,generics
from . import serializers
from django.core.email import send_email
import random
from .models import User

# Create your views here.


#first let's create sned email 
def send_email(email):
    subject = 'VERIFICATION EMAIL'
    otp = random.randint(10001, 99999)
    messages = f"Your verification code is {otp}"
    email_from = settings.EMAIL_HOST
    send_email(subject,messages,email_from,[email],fail_silently=False)
    user_obj = User.objects.all(email=email)
    user_obj.otp = otp
    