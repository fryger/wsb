# Generated by Django 3.1.7 on 2022-01-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_auto_20220103_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='plate',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]