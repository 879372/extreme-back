from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("clients", "0002_client_billing_fields")]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
