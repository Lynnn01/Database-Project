# Generated by Django 5.0 on 2024-01-17 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
    ]