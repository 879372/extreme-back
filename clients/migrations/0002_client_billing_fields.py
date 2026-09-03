from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("clients", "0001_initial")]

    operations = [
        migrations.AddField(model_name="client", name="system_url", field=models.URLField(blank=True)),
        migrations.AddField(model_name="client", name="billing_day", field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])),
        migrations.AddField(model_name="client", name="billing_messages_enabled", field=models.BooleanField(default=False)),
        migrations.AddField(model_name="client", name="last_billing_message_at", field=models.DateField(blank=True, editable=False, null=True)),
    ]
