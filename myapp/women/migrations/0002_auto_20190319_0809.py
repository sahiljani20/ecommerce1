# Generated by Django 2.1.4 on 2019-03-19 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wo_product',
            old_name='price',
            new_name='pri',
        ),
    ]
