# Generated by Django 5.0 on 2024-01-23 18:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0003_alter_order_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateField(default=datetime.datetime(2024, 1, 23, 18, 4, 58, 455862, tzinfo=datetime.timezone.utc)),
        ),
    ]
