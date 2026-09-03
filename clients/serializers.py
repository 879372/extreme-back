from rest_framework import serializers
from .models import BillingSettings, Charge, Client
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class BillingSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingSettings
        fields = "__all__"


class ChargeSerializer(serializers.ModelSerializer):
    client_company = serializers.CharField(source="client.company", read_only=True)
    client_name = serializers.CharField(source="client.full_name", read_only=True)
    client_phone = serializers.CharField(source="client.phone", read_only=True)

    class Meta:
        model = Charge
        fields = "__all__"
        read_only_fields = ("paid_at",)
