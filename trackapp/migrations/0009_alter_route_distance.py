# Generated by Django 5.0.6 on 2024-06-19 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackapp', '0008_route_trip_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='distance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
