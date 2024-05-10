# Generated by Django 4.2.7 on 2024-04-26 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("addnam", models.CharField(max_length=255, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Mouhafaza",
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
                ("mounam", models.CharField(max_length=255, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Pharmain",
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
                ("phanam", models.CharField(max_length=255, null=True, unique=True)),
                (
                    "phacistnam",
                    models.CharField(max_length=255, null=True, unique=True),
                ),
                ("phonam", models.CharField(max_length=255, null=True, unique=True)),
                (
                    "address",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pharma.address",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Casa",
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
                ("casnam", models.CharField(max_length=255, null=True, unique=True)),
                (
                    "mouhafaza",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pharma.mouhafaza",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="address",
            name="casa",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="pharma.casa"
            ),
        ),
    ]