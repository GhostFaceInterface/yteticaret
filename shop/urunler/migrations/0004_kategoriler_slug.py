# Generated by Django 5.1.5 on 2025-01-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("urunler", "0003_kategoriler_seo_description_kategoriler_seo_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="kategoriler",
            name="slug",
            field=models.SlugField(blank=True, max_length=155, null=True, unique=True),
        ),
    ]
