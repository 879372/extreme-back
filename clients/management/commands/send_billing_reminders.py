import calendar
import os

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from clients.evolution import EvolutionError, send_text
from clients.models import Client


DEFAULT_TEMPLATE = "Olá, {name}! Passando para lembrar que a mensalidade de {value} da {company} vence hoje. Qualquer dúvida, estou à disposição. — Kaibez"


class Command(BaseCommand):
    help = "Envia lembretes de cobrança do dia pela Evolution Go."

    def add_arguments(self, parser):
        parser.add_argument("--dry-run", action="store_true", help="Lista os envios sem chamar o WhatsApp.")

    def handle(self, *args, **options):
        today = timezone.localdate()
        last_day = calendar.monthrange(today.year, today.month)[1]
        clients = Client.objects.filter(billing_messages_enabled=True, status__in=[Client.Status.ACTIVE, Client.Status.ONBOARDING]).exclude(last_billing_message_at=today)
        clients = [client for client in clients if client.billing_day == today.day or (today.day == last_day and client.billing_day and client.billing_day > last_day)]

        if not options["dry_run"] and os.environ.get("EVOLUTION_GO_ENABLED", "False").lower() != "true":
            raise CommandError("Envio desabilitado. Configure EVOLUTION_GO_ENABLED=True após validar as credenciais.")

        template = os.environ.get("EVOLUTION_GO_BILLING_TEMPLATE", DEFAULT_TEMPLATE)
        sent = 0
        for client in clients:
            message = template.format(name=client.full_name, company=client.company, value=f"R$ {client.monthly_value:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), system_url=client.system_url)
            if options["dry_run"]:
                self.stdout.write(f"[SIMULAÇÃO] {client.company} -> {client.phone}: {message}")
                continue
            try:
                send_text(client.phone, message)
            except EvolutionError as error:
                self.stderr.write(f"Falha para {client.company}: {error}")
                continue
            client.last_billing_message_at = today
            client.save(update_fields=["last_billing_message_at", "updated_at"])
            sent += 1
            self.stdout.write(self.style.SUCCESS(f"Enviado para {client.company}"))

        self.stdout.write(f"Concluído: {sent} envio(s); {len(clients)} cobrança(s) encontrada(s).")
