from rest_framework import serializers
from .models import Client, ClientAddress,ClientService


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'mobile_number', 'image', 'account_holder_name',
                  'account_number', 'MCIR_code', 'IFSC_code', 'name_of_bank', 'client_type']


class ClientAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAddress
        fields = ['id', 'street_address', 'city', 'state', 'postal_pin_code']

class ClientServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientService
        fields = ['id', 'title', 'rate', 'other']
