# Generated by Django 4.0.4 on 2022-06-03 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0005_rename_price_per_km_rider_trip_extra1_distance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_pick_form',
            name='select_truck_type',
        ),
    ]
