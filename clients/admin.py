from django.contrib import admin
from .models import BillingSettings, Charge, Client
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("company", "full_name", "service", "status", "monthly_value", "billing_day", "billing_messages_enabled")
    list_filter = ("status", "service", "billing_messages_enabled")
    search_fields = ("company", "full_name", "email")


@admin.register(Charge)
class ChargeAdmin(admin.ModelAdmin):
    list_display = ("client", "due_date", "amount", "status", "paid_at")
    list_filter = ("status", "due_date")
    search_fields = ("client__company", "client__full_name")


admin.site.register(BillingSettings)
