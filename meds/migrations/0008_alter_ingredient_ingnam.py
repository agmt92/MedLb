# Generated by Django 4.2.7 on 2024-04-04 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meds", "0007_rescountry_resparty_remove_drug_strength_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingredient",
            name="ingnam",
            field=models.CharField(max_length=550, null=True, unique=True),
        ),
    ]
