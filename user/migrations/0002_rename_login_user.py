# Generated by Django 4.0.3 on 2022-05-30 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Login',
            new_name='User',
        ),
    ]
