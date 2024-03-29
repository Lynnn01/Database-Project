# Generated by Django 5.0 on 2024-01-16 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('stock', models.IntegerField(default=0)),
                ('isTrending', models.BooleanField(default=False)),
                ('image', models.ImageField(default='img/None/no-img.jpg', upload_to='products/')),
            ],
        ),
    ]
