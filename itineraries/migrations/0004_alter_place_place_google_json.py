# Generated by Django 4.2 on 2023-04-19 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itineraries', '0003_rename_place_json_info_place_place_google_json_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_google_json',
            field=models.JSONField(default={'details': 'This place does not have a Google Places JSON attached.'}),
        ),
    ]