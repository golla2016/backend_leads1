from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

from django.db import models

class Agent(models.Model):
    CONTACT_METHOD_CHOICES = [
        ("WhatsApp Only", "WhatsApp Only"),
        ("Telegram Only", "Telegram Only"),
        ("Both", "Both"),
    ]
    
    RECEIPT_METHOD_CHOICES = [
        ("UPI", "UPI"),
        ("Bank", "Bank"),
    ]

    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10, unique=True)
    contact_method = models.CharField(max_length=20, choices=CONTACT_METHOD_CHOICES)
    # receipt_method = models.CharField(max_length=10, choices=RECEIPT_METHOD_CHOICES, blank=True, null=True)
    
    # upi_id = models.CharField(max_length=50, blank=True, null=True)  # For UPI payment
    # bank_account = models.CharField(max_length=18, blank=True, null=True)  # For Bank Transfer
    # ifsc_code = models.CharField(max_length=11, blank=True, null=True)
    password = models.CharField(max_length=128, blank = True, null=True) # Store hashed password
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)
    secretQuestion = models.CharField(max_length=200, blank=True, null=True)
    secretAnswer = models.CharField(max_length=200, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        # Hash password before saving (only if it's a new password)
        if self.password and not self.password.startswith("pbkdf2_"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.first_name} {self.surname} - {self.mobile}"

