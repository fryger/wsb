# Generated by Django 3.1.7 on 2021-08-30 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_gps'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='token',
            field=models.CharField(default='asd', max_length=32),
            preserve_default=False,
        ),
    ]
