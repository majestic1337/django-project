# Generated by Django 4.2.8 on 2023-12-07 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_order_ph'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ph',
        ),
        migrations.AddField(
            model_name='order',
            name='ogfd',
            field=models.TextField(default='d'),
        ),
    ]
