# Generated by Django 4.2.8 on 2023-12-07 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_order_num'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='num',
            new_name='ph',
        ),
    ]