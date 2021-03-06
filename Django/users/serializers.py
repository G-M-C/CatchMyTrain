from django.db import models
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        #user['email'] = validated_data['email']
        #user['full_name'] = validated_data['full_name']
        return user

    class Meta:
        model = User 
        fields = [    
            "username",
            "full_name",          
            "password",
            "email",
            "phoneNo",
            "age",
        ]
       
class SetUserDataSerializer(serializers.Serializer):

    token = serializers.CharField(max_length=255, required=True)
    full_name = serializers.CharField(max_length=255, required=False, default=None)
    email = serializers.EmailField(max_length=255, min_length=None, allow_blank=False, required=False, default=None)
    phoneNo = serializers.CharField(max_length=15, required=False, default=None)
    age = serializers.IntegerField(required=False, default=None)


        
class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=None, min_length=None, allow_blank=False)
    password = serializers.CharField(allow_blank=False)

   
class UserIDSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=32)


    
