# Generated by Django 5.0.6 on 2024-07-08 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_device_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="device",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="uploads/"),
        ),
        migrations.AddField(
            model_name="device",
            name="thumbnail",
            field=models.ImageField(blank=True, null=True, upload_to="uploads/"),
        ),
    ]
