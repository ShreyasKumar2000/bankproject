# Generated by Django 4.2.5 on 2023-12-14 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_country_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='district',
        ),
        migrations.RemoveField(
            model_name='city',
            name='country',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='account_type',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='district',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='materials_provide',
        ),
        migrations.DeleteModel(
            name='AccountType',
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='District',
        ),
        migrations.DeleteModel(
            name='Material',
        ),
    ]
