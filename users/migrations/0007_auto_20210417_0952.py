# Generated by Django 2.2 on 2021-04-17 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210412_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=30, unique=True, verbose_name='phone number'),
        ),
    ]