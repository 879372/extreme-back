from django.db import migrations, models


def rebrand_existing_messages(apps, schema_editor):
    BillingSettings = apps.get_model("clients", "BillingSettings")
    for settings in BillingSettings.objects.filter(message_template__icontains="Extreme Software"):
        settings.message_template = settings.message_template.replace("Extreme Software", "Kaibez")
        settings.save(update_fields=["message_template"])


class Migration(migrations.Migration):
    dependencies = [("clients", "0004_billing_settings_and_charges")]

    operations = [
        migrations.AlterField(
            model_name="billingsettings",
            name="message_template",
            field=models.TextField(default="Olá, {name}! A mensalidade de {value} da {company} está pendente. Chave PIX: {pix_key}. Obrigado! — Kaibez"),
        ),
        migrations.RunPython(rebrand_existing_messages, migrations.RunPython.noop),
    ]
