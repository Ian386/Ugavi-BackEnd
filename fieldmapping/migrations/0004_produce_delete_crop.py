# Generated by Django 5.0.6 on 2024-06-13 06:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fieldmapping', '0003_remove_crop_name_crop_variety'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produce_type', models.CharField(max_length=100)),
                ('variety', models.CharField(blank=True, max_length=225)),
                ('description', models.TextField(blank=True, null=True)),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crops', to='fieldmapping.farm')),
            ],
            options={
                'verbose_name_plural': 'Crops',
            },
        ),
        migrations.DeleteModel(
            name='Crop',
        ),
    ]
