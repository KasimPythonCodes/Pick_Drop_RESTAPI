# Generated by Django 4.0.4 on 2022-06-03 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0006_remove_user_pick_form_select_truck_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike_Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basefare', models.FloatField()),
                ('basekm', models.FloatField()),
                ('price1_per_km', models.FloatField(blank=True, null=True)),
                ('price2_per_km', models.FloatField(blank=True, null=True)),
                ('price3_per_km', models.FloatField(blank=True, null=True)),
                ('price4_per_km', models.FloatField(blank=True, null=True)),
                ('price5_per_km', models.FloatField(blank=True, null=True)),
                ('price6_per_km', models.FloatField(blank=True, null=True)),
                ('extra1_distance', models.FloatField(blank=True, null=True)),
                ('extra2_distance', models.FloatField(blank=True, null=True)),
                ('extra3_distance', models.FloatField(blank=True, null=True)),
                ('extra4_distance', models.FloatField(blank=True, null=True)),
                ('extra5_distance', models.FloatField(blank=True, null=True)),
                ('extra6_distance', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]