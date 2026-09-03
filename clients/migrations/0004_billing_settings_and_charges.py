from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [("clients", "0003_make_client_email_optional")]

    operations = [
        migrations.CreateModel(
            name="BillingSettings",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("pix_key", models.CharField(blank=True, max_length=160)),
                ("message_template", models.TextField(default="Olá, {name}! A mensalidade de {value} da {company} está pendente. Chave PIX: {pix_key}. Obrigado! — Extreme Software")),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"verbose_name": "Configuração de cobrança", "verbose_name_plural": "Configurações de cobrança"},
        ),
        migrations.CreateModel(
            name="Charge",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("due_date", models.DateField()),
                ("amount", models.DecimalField(decimal_places=2, max_digits=12)),
                ("status", models.CharField(choices=[("Pendente", "Pendente"), ("Pago", "Pago")], default="Pendente", max_length=20)),
                ("paid_at", models.DateTimeField(blank=True, editable=False, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("client", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="charges", to="clients.client")),
            ],
            options={"ordering": ["status", "due_date"]},
        ),
        migrations.AddConstraint(model_name="charge", constraint=models.UniqueConstraint(fields=("client", "due_date"), name="unique_client_charge_due_date")),
    ]
