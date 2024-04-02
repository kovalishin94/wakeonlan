from django.db import models

class Computer(models.Model):
    ip_address = models.CharField(max_length=255, unique=True)
    mac_address = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["ip_address"]