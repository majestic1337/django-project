# Generated by Django 4.2.8 on 2023-12-07 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_rename_ogfd_order_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.AddField(
            model_name='order',
            name='phone_num',
            field=models.CharField(default='+380', max_length=30),
        ),
    ]
