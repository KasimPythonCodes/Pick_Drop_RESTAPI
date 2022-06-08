# Generated by Django 4.0.4 on 2022-06-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PICKFORM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_point', models.CharField(max_length=256)),
                ('drop_point', models.CharField(max_length=256)),
                ('distance', models.FloatField(blank=True, max_length=256, null=True)),
                ('total_price', models.FloatField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]