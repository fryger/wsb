# Generated by Django 3.1.7 on 2021-08-30 14:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.car')),
            ],
        ),
    ]