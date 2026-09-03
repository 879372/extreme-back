from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=160)),
                ("company", models.CharField(max_length=160)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone", models.CharField(max_length=30)),
                ("service", models.CharField(max_length=120)),
                ("status", models.CharField(choices=[("Ativo", "Ativo"), ("Onboarding", "Onboarding"), ("Pausado", "Pausado")], default="Onboarding", max_length=20)),
                ("monthly_value", models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
