# Generated by Django 4.2 on 2023-04-19 17:02

from django.db import migrations, models
import itineraries.models


class Migration(migrations.Migration):

    dependencies = [
        ('itineraries', '0005_alter_place_place_google_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_google_json',
            field=models.JSONField(default=itineraries.models.place_json_placeholder),
        ),
    ]