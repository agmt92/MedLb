# Generated by Django 4.2.7 on 2024-04-27 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pharma", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Phones",
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
                ("phonam", models.CharField(max_length=255, null=True, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="pharmain",
            name="phonam",
        ),
        migrations.AddField(
            model_name="pharmain",
            name="phones",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="pharma.phones",
            ),
        ),
    ]
