from django.db import models
from agents.models import Agent

class UserSubmission(models.Model):
    CONTACT_METHOD_CHOICES = [
        ("WhatsApp Only", "WhatsApp Only"),
        ("Telegram Only", "Telegram Only"),
        ("Both", "Both"),
    ]

    COVER_TYPE_CHOICES = [
        ("Individual", "Individual"),
        ("Floater", "Floater"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)
    contact_method = models.CharField(max_length=20, choices=CONTACT_METHOD_CHOICES)
    pincode = models.CharField(max_length=6)
    total_members = models.IntegerField()
    cover_type = models.CharField(max_length=20, choices=COVER_TYPE_CHOICES)
    adults = models.IntegerField()
    children = models.IntegerField()
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, blank=True, related_name="submissions")
    additional_comments = models.TextField(blank=True, null=True)
    unique_id = models.CharField(max_length=20, unique=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"

