from rest_framework import viewsets
from .models import BillingSettings, Charge, Client
from .serializers import BillingSettingsSerializer, ChargeSerializer, ClientSerializer
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class BillingSettingsViewSet(viewsets.ModelViewSet):
    queryset = BillingSettings.objects.all()
    serializer_class = BillingSettingsSerializer


class ChargeViewSet(viewsets.ModelViewSet):
    queryset = Charge.objects.select_related("client").all()
    serializer_class = ChargeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        client_id = self.request.query_params.get("client")
        return queryset.filter(client_id=client_id) if client_id else queryset
