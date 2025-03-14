from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserSubmissionViewSet

router = DefaultRouter()
router.register(r'customer-forms', UserSubmissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
