# Generated by Django 4.2 on 2024-11-28 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone_number", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="ServiceRequest",
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
                (
                    "service_type",
                    models.CharField(
                        choices=[
                            ("GAS_LEAK", "Gas Leak"),
                            ("INSTALLATION", "New Installation"),
                            ("MAINTENANCE", "Maintenance"),
                        ],
                        max_length=20,
                    ),
                ),
                ("description", models.TextField()),
                (
                    "attached_file",
                    models.FileField(blank=True, null=True, upload_to="attachments/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer_service.customer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RequestStatus",
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
                ("status", models.CharField(default="Pending", max_length=50)),
                ("resolved_at", models.DateTimeField(blank=True, null=True)),
                (
                    "request",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer_service.servicerequest",
                    ),
                ),
            ],
        ),
    ]
