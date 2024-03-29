# Generated by Django 4.2 on 2023-04-28 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('created_by', models.IntegerField()),
                ('archived', models.BooleanField(default=False)),
                ('private', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('forked_from', models.IntegerField(blank=True, default=None, null=True)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('city', models.CharField(default='PLACEHOLDER_CITY', max_length=255)),
                ('state', models.CharField(default='PLACEHOLDER_STATE', max_length=255)),
                ('country', models.CharField(default='PLACEHOLDER_COUNTRY', max_length=255)),
                ('title', models.CharField(default='Untitiled', max_length=255)),
                ('description', models.CharField(default='This itinerary does not have a description yet...', max_length=1024)),
                ('est_budget_up', models.IntegerField(default=10)),
                ('est_budget_down', models.IntegerField(default=0)),
                ('itinerary', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('place_id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField()),
                ('place_json', models.JSONField()),
            ],
        ),
    ]
