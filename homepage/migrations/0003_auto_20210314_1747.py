# Generated by Django 3.1.7 on 2021-03-14 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20210314_1744'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Newsletter',
            new_name='NewsletterSubscribers',
        ),
    ]