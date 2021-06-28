from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Invoice, InvoiceService


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'client', 'gst', 'total']


class InvoiceServiceSerializer(serializers.ModelSerializer):
    class Meta:
        models = InvoiceService
        fields = ['id', 'client', 'service', 'count', 'total']
