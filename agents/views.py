from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Agent
from .serializers import AgentSerializer, AgentBusinessSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
import gspread
import json
import os
from rest_framework.views import APIView
from rest_framework.response import Response

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class AgentsListAPIView(APIView):
    def get(self, request):
        service_account_json = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")
        sheet_id = os.environ.get("GOOGLE_SHEET_ID")
        # 🔎 Debug checks
        if not service_account_json:
            return Response({"error": "GOOGLE_SERVICE_ACCOUNT_JSON is missing"}, status=500)
        if not sheet_id:
            return Response({"error": "GOOGLE_SHEET_ID is missing"}, status=500)
        try: 
            service_account_info = json.loads(service_account_json)
            sheet_id = os.environ.get("GOOGLE_SHEET_ID")
            gc = gspread.service_account_from_dict(service_account_info)
            
            sh = gc.open_by_key(sheet_id)
            worksheet = sh.worksheet("Agents")
            rows = worksheet.get_all_values()
            agents = [{"id": row[0], "first_name": row[1], "surname": row[2]} for row in rows[1:]]
            return Response(agents)
        except Exception as e:
            return Response({"error": f"Invalid JSON format: {str(e)}"}, status=500)
        # ✅ If we reached here, JSON is valid
        return Response({"message": "Service account JSON loaded successfully!"})

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

