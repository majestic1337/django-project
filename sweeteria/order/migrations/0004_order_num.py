# Generated by Django 4.2.8 on 2023-12-07 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_remove_order_mob_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='num',
            field=models.CharField(default='+38000000000', max_length=20),
        ),
    ]
