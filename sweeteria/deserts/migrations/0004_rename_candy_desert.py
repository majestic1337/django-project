# Generated by Django 4.2.8 on 2024-10-29 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deserts', '0003_alter_candy_img_path'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Candy',
            new_name='Desert',
        ),
    ]
