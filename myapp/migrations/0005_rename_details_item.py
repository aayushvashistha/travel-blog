# Generated by Django 4.2.1 on 2023-06-09 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='details',
            new_name='item',
        ),
    ]
