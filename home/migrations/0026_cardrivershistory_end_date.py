# Generated by Django 3.1.7 on 2021-10-24 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20211020_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardrivershistory',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
