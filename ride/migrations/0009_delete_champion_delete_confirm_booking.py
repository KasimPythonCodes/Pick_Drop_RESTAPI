# Generated by Django 4.0.4 on 2022-06-28 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0008_rename_user_vehicle_confirm_booking_user_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='champion',
        ),
        migrations.DeleteModel(
            name='Confirm_Booking',
        ),
    ]
