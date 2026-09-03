from django.db import models

class Client(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "Ativo", "Ativo"
        ONBOARDING = "Onboarding", "Onboarding"
        PAUSED = "Pausado", "Pausado"
    full_name = models.CharField(max_length=160)
    company = models.CharField(max_length=160)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30)
    service = models.CharField(max_length=120)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ONBOARDING)
    monthly_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-created_at"]
    def __str__(self):
        return f"{self.company} — {self.full_name}"
