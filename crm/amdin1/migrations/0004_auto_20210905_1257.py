# Generated by Django 3.0.7 on 2021-09-05 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amdin1', '0003_admin_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_register',
            name='mobile_number',
            field=models.IntegerField(),
        ),
    ]
