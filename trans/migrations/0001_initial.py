# Generated by Django 4.0.3 on 2022-05-28 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowDate', models.DateField(blank=True, null=True)),
                ('returnDate', models.DateField(blank=True, null=True)),
                ('theBook', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='book.book')),
                ('theCustomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]