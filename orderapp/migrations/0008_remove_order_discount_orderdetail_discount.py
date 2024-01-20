# Generated by Django 5.0 on 2024-01-17 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0007_order_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='discount',
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]
