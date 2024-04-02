from django.contrib import admin
from core import models


@admin.register(models.Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = (
        'ip_address', 
        'mac_address', 
        'created_at', 
        'updated_at'
        )
