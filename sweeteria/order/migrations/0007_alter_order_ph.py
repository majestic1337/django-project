# Generated by Django 4.2.8 on 2023-12-07 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_rename_num_order_ph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ph',
            field=models.FloatField(),
        ),
    ]
