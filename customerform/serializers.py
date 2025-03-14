from rest_framework import serializers
from .models import UserSubmission
from agents.models import Agent

class UserSubmissionSerializer(serializers.ModelSerializer):
    agent_name = serializers.CharField(source="agent.first_name", read_only=True)  # Show agent's name

    class Meta:
        model = UserSubmission
        fields = "__all__"

    # def validate(self, data):
    #     # Ensure UPI ID is provided if receipt method is UPI
    #     if data.get("cover_type") == "Individual" and data.get("total_members") > 1:
    #         raise serializers.ValidationError({"total_members": "Individual cover cannot have more than 1 member."})
        
    #     # Ensure agent exists
    #     agent_id = self.initial_data.get("agent")
    #     if agent_id and not Agent.objects.filter(id=agent_id).exists():
    #         raise serializers.ValidationError({"agent": "Agent does not exist."})

    #     return data
