# Generated by Django 4.0.4 on 2022-06-29 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Userform', '0002_alter_pickform_user_vehicle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pickform',
            name='price_t',
        ),
        migrations.RemoveField(
            model_name='pickform',
            name='user_vehicle',
        ),
    ]
