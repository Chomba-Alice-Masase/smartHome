# Generated by Django 5.1.2 on 2024-10-16 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_sensordata_distance_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sensordata',
            options={},
        ),
        migrations.RemoveField(
            model_name='sensordata',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='humidity',
            field=models.FloatField(default=0.0),
        ),
    ]