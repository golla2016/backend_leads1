from rest_framework import viewsets
from .models import UserSubmission
from .serializers import UserSubmissionSerializer
from agents.models import Agent
from rest_framework import serializers

class UserSubmissionViewSet(viewsets.ModelViewSet):
    queryset = UserSubmission.objects.all().select_related("agent")  # Optimize queries
    serializer_class = UserSubmissionSerializer

    def perform_create(self, serializer):
        print("Received Data:", self.request.data)
        agent_id = self.request.data.get("agent")
        if agent_id:
            try:
                agent = Agent.objects.get(id=agent_id)  # ✅ Get the agent object
                serializer.save(agent=agent)  # ✅ Assign the object, not ID
            except Agent.DoesNotExist:
                raise serializers.ValidationError({"agent": "Agent not found."})
        else:
            serializer.save()



