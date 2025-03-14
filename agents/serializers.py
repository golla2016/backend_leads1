from rest_framework import serializers
from .models import Agent
from customerform.models import UserSubmission

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = "__all__"

    def validate(self, data):
        # Ensure UPI ID is provided if receipt method is UPI
        if data.get("receipt_method") == "UPI" and not data.get("upi_id"):
            raise serializers.ValidationError({"upi_id": "UPI ID is required for UPI payment."})
        
        # Ensure Bank details are provided if receipt method is Bank
        if data.get("receipt_method") == "Bank" and not data.get("bank_account"):
            raise serializers.ValidationError({"bank_account": "Bank Account Number is required for Bank Transfer."})
        
        return data

class UserSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubmission
        fields = ["id", "name", "email", "phone", "total_members", "cover_type", "created_at"]  # Only necessary fields

class AgentBusinessSerializer(serializers.ModelSerializer):    
    submissions = UserSubmissionSerializer(many=True, read_only=True)  # Include related customers
    class Meta:
        model = Agent
        # ✅ Explicitly define field order (submissions at the end)
        fields = [
            "id",
            "first_name",
            "surname",
            "mobile",
            "contact_method",
            # "receipt_method",
            # "upi_id",
            # "bank_account",
            # "ifsc_code",
            "profile_picture",
            "created_at",
            "submissions"  # ✅ Move this to the end
        ]