# Generated by Django 4.0.4 on 2022-06-02 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0003_remove_rider_trip_distance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rider_trip',
            name='price_per_km',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
