from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Agent
from .serializers import AgentSerializer, AgentBusinessSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    

class AgentBusinessViewSet(viewsets.ReadOnlyModelViewSet):  # ✅ ReadOnly to prevent modifications
    queryset = Agent.objects.prefetch_related("submissions").all()  # Optimized query
    serializer_class = AgentBusinessSerializer
    
@api_view(["POST"])
def agent_login(request):
    mobile = request.data.get("mobile")
    password = request.data.get("password")

    agent = get_object_or_404(Agent, mobile=mobile)

    if agent.check_password(password):  # ✅ Verify hashed password
        return Response({"success": True, "agent_id": agent.id}, status=200)
    else:
        return Response({"success": False, "message": "Invalid credentials"}, status=400)
    
@api_view(["POST"])
def update_password(request):
    mobile = request.data.get("mobile")
    
    password = request.data.get("password")

    # Check if agent exists
    agent = get_object_or_404(Agent, mobile=mobile)

    

    # Update the password securely
    agent.password = make_password(password)
    agent.save()

    return Response({"success": True, "message": "Password updated successfully"}, status=200)

