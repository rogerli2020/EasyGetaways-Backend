# Generated by Django 4.2 on 2023-04-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itineraries', '0004_alter_place_place_google_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_google_json',
            field=models.JSONField(default={'details': 'This Place does not have a Google Places JSON attached.'}),
        ),
    ]
