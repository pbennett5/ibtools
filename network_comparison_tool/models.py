# models.py
from django.db import models

class Provider(models.Model):
    country = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    subregion = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    provider = models.CharField(max_length=100, null=True, blank=True)
    building_address = models.CharField(max_length=255, null=True, blank=True)
    license_number = models.CharField(max_length=100, null=True, blank=True)
    special_notes = models.TextField(null=True, blank=True)
    pobox = models.CharField(max_length=100, null=True, blank=True)
    provider_startdate = models.DateField(null=True, blank=True)
    telephone = models.CharField(max_length=100, null=True, blank=True)
    fax = models.CharField(max_length=100, null=True, blank=True)
    has_dental_service = models.BooleanField(null=True, blank=True)
    provider_group = models.CharField(max_length=100, null=True, blank=True)
    # Add more fields based on the other insurance companies

