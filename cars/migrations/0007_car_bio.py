# Generated by Django 5.1.1 on 2024-10-22 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0006_carinventory"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
    ]