# Generated by Django 3.1.7 on 2021-03-12 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20210311_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='lineitem_total',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
