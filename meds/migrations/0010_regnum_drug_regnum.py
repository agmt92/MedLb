# Generated by Django 4.2.7 on 2024-04-04 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("meds", "0009_regnum_alter_ingredient_ingnam_drug_regnum"),
    ]

    operations = [
        migrations.CreateModel(
            name="Regnum",
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
                ("regnam", models.CharField(max_length=255, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="drug",
            name="regnum",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="meds.regnum"
            ),
        ),
    ]
