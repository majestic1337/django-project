# Generated by Django 4.2.8 on 2023-12-07 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_remove_order_ph_order_ogfd'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='ogfd',
            new_name='name',
        ),
    ]