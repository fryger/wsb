# Generated by Django 3.1.7 on 2021-08-31 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_carservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenance',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.carservice'),
        ),
    ]
