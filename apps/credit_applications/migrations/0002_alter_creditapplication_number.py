# Generated by Django 4.2.1 on 2023-06-04 15:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("credit_applications", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="creditapplication",
            name="number",
            field=models.CharField(unique=True),
        ),
    ]