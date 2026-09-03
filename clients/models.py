from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

class Client(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "Ativo", "Ativo"
        ONBOARDING = "Onboarding", "Onboarding"
        PAUSED = "Pausado", "Pausado"
    full_name = models.CharField(max_length=160)
    company = models.CharField(max_length=160)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=30)
    service = models.CharField(max_length=120)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ONBOARDING)
    monthly_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    system_url = models.URLField(blank=True)
    billing_day = models.PositiveSmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    billing_messages_enabled = models.BooleanField(default=False)
    last_billing_message_at = models.DateField(null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-created_at"]
    def __str__(self):
        return f"{self.company} — {self.full_name}"


class BillingSettings(models.Model):
    pix_key = models.CharField(max_length=160, blank=True)
    message_template = models.TextField(default="Olá, {name}! A mensalidade de {value} da {company} está pendente. Chave PIX: {pix_key}. Obrigado! — Extreme Software")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Configuração de cobrança"
        verbose_name_plural = "Configurações de cobrança"

    def __str__(self):
        return "Configurações de cobrança"


class Charge(models.Model):
    class Status(models.TextChoices):
        PENDING = "Pendente", "Pendente"
        PAID = "Pago", "Pago"

    client = models.ForeignKey(Client, related_name="charges", on_delete=models.CASCADE)
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    paid_at = models.DateTimeField(null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["status", "due_date"]
        constraints = [models.UniqueConstraint(fields=["client", "due_date"], name="unique_client_charge_due_date")]

    def save(self, *args, **kwargs):
        if self.status == self.Status.PAID and not self.paid_at:
            self.paid_at = timezone.now()
        elif self.status == self.Status.PENDING:
            self.paid_at = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.client.company} — {self.due_date} — {self.status}"
