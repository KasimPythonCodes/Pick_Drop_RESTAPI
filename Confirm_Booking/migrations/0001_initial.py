# Generated by Django 4.0.4 on 2022-06-28 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Confirm_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_point', models.CharField(blank=True, max_length=256, null=True)),
                ('drop_point', models.CharField(blank=True, max_length=256, null=True)),
                ('price', models.FloatField()),
                ('distance', models.FloatField()),
                ('vehicle', models.CharField(blank=True, max_length=256, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
