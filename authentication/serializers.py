from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=2, max_length=100)
    first_name = serializers.CharField(min_length=2, max_length=100)
    last_name = serializers.CharField(min_length=2, max_length=100)
    email = serializers.EmailField(min_length=4, max_length=255)
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
