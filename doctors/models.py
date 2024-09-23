from django.db import models

from main.models import BaseModel


class Doctor(BaseModel):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    specialization = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255)
    biography = models.TextField(null=True, blank=True)
