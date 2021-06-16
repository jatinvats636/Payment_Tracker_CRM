from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(min_length=2,max_length=100)
    last_name=serializers.CharField(min_length=2,max_length=100)
    email=serializers.EmailField(min_length=6,max_length=255)
    password=serializers.CharField(min_length=6,max_length=65,write_only=True)


    class Meta:
        model = User
        fields=['first_name','last_name','email','password']

    def validate(self,data):
        email=data.get('email','')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('Email Already Exists')})
        return super().validate(data)

    def create(self,validated_data):
        User.objects.create_user(**validated_data)

