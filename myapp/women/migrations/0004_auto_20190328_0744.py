# Generated by Django 2.1.4 on 2019-03-28 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0003_wo_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wo_product',
            name='image',
            field=models.ImageField(default='', upload_to='images/women/'),
        ),
    ]
