# Generated by Django 5.1.5 on 2025-01-29 17:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("urunler", "0009_varyasyonlar"),
    ]

    operations = [
        migrations.AddField(
            model_name="varyasyonlar",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="urunler.varyasyonlar",
            ),
        ),
    ]
