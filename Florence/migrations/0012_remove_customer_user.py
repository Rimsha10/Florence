# Generated by Django 4.0.5 on 2022-07-01 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Florence', '0011_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
