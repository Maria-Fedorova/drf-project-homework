# Generated by Django 5.1.3 on 2024-11-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_payment_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="payment_method",
            field=models.CharField(
                choices=[("Cash", "cash"), ("Transaction", "transaction")],
                default="Cash",
                verbose_name="Способ оплаты",
            ),
        ),
    ]