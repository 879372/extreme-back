from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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
