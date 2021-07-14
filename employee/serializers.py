from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["name", "designation", "email", "mobile_number", "address", "salary",
                  "incentives", "other", "status", "payment_date",
                  "joining_date", "description", "account_holder_name", "account_number",
                  "MCIR_code", "IFSC_code", "name_of_bank", "image"]
