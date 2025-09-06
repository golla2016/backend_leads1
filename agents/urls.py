from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgentViewSet, AgentBusinessViewSet, agent_login, update_password, AgentsListAPIView

router = DefaultRouter()
router.register(r'agents', AgentViewSet) # ✅ For CRUD
router.register(r'agents-business', AgentBusinessViewSet, basename="agents-business")  # ✅ New business endpoint


urlpatterns = [
    path('', include(router.urls)),
    path("agent-login/", agent_login, name="agent-login"),
    path("update-password/", update_password, name="update-password"),
    path("get-agents/", AgentsListAPIView.as_view() , name="get-agents"),
]
