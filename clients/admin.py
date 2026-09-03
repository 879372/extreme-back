from django.contrib import admin
from .models import Client
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("company", "full_name", "service", "status", "monthly_value")
    list_filter = ("status", "service")
    search_fields = ("company", "full_name", "email")
