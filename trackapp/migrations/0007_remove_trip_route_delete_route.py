# Generated by Django 5.0.6 on 2024-06-19 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackapp', '0006_route_trip_route'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='route',
        ),
        migrations.DeleteModel(
            name='Route',
        ),
    ]
