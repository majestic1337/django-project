# Generated by Django 4.2.8 on 2023-12-14 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.CharField(default='', max_length=50),
        ),
    ]