# Generated by Django 4.0.3 on 2022-05-28 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trans',
            old_name='theBook',
            new_name='bookName',
        ),
    ]
