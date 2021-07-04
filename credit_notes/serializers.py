from rest_framework import serializers
from .models import CreditNotes


class CreditNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditNotes
        fields = ['id', 'invoice', 'created_at', 'reason', 'payment_terms','status']