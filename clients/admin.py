from django.contrib import admin
from .models import Client
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("company", "full_name", "service", "status", "monthly_value", "billing_day", "billing_messages_enabled")
    list_filter = ("status", "service", "billing_messages_enabled")
    search_fields = ("company", "full_name", "email")
