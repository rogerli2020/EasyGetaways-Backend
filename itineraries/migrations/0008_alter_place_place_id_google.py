# Generated by Django 4.2 on 2023-04-19 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itineraries', '0007_alter_place_place_google_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_id_google',
            field=models.CharField(default=None, max_length=127, null=True),
        ),
    ]
