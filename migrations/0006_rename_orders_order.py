# Generated by Django 4.1.5 on 2023-04-15 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders_delete_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
