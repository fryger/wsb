# Generated by Django 3.1.7 on 2021-08-13 16:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20210813_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='nip',
            field=models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
