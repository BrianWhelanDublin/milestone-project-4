# Generated by Django 3.1.7 on 2021-03-21 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
        ('wishlist', '0004_auto_20210321_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userswishlist',
            name='items',
            field=models.ManyToManyField(blank=True, to='stock.Item'),
        ),
    ]
