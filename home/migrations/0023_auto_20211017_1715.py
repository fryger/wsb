# Generated by Django 3.1.7 on 2021-10-17 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20211016_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gps',
            name='alt',
            field=models.FloatField(blank=True, null=True),
        ),
    ]