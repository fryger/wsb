# Generated by Django 3.1.7 on 2021-08-30 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_car_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='token',
        ),
    ]