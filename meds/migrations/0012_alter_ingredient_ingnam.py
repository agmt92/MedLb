# Generated by Django 4.2.7 on 2024-04-04 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meds", "0011_alter_ingredient_ingnam"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingredient",
            name="ingnam",
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
