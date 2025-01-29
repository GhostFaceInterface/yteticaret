# Generated by Django 5.1.5 on 2025-01-22 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("urunler", "0004_kategoriler_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="markalar",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("isim", models.CharField(max_length=155)),
                ("aciklama", models.TextField(blank=True, null=True)),
                ("seo_title", models.CharField(blank=True, max_length=155, null=True)),
                ("seo_description", models.TextField(blank=True, null=True)),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=155, null=True, unique=True
                    ),
                ),
                ("aktifmi", models.BooleanField(default=True)),
                (
                    "resim",
                    models.ImageField(
                        blank=True, null=True, upload_to="markaresimleri"
                    ),
                ),
            ],
            options={
                "verbose_name": "Marka",
                "verbose_name_plural": "Markalar",
            },
        ),
    ]
