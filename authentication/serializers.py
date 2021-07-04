from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomSessionModel


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=2, max_length=100)
    first_name = serializers.CharField(min_length=2, max_length=100)
    last_name = serializers.CharField(min_length=2, max_length=100)
    email = serializers.EmailField(min_length=4, max_length=255,)
    password = serializers.CharField(
        min_length=6, max_length=100, write_only=True)

    class META:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def validate(self, data):
        email = data.get('email', None)
        username = data.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'username': ('Username is already in use')})
        return super().validate(data)
      
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, min_length=2)
    password=serializers.CharField(max_length=65, min_length=8, write_only=True)

    class Meta:
        model=User
        fields=['username','password']

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self,attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self,**kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            return 'Token is expired or invalid'
