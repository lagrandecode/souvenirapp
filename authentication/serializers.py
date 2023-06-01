from rest_framework import serializers
from .models import User


from rest_framework import serializers





class UserCreationSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    name = serializers.CharField(max_length=50)
=======
    # name = serializers.CharField(max_length=50)
>>>>>>> 99e43c5666d148afb58d8fb3ff5ace94a91960da
    email = serializers.EmailField(max_length=80)
    phone_number = serializers.CharField(max_length=14)
    password = serializers.CharField(max_length=18,write_only=True)
    address = serializers.CharField(max_length=50)
    isVerified = serializers.BooleanField(default=False)

    class Meta:
        model=User
        fields=['name','email','phone_number','password','address','isVerified']


class VerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()







