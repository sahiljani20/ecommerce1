# Generated by Django 2.1.4 on 2019-04-04 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0006_auto_20190329_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wo_product',
            name='catagories',
            field=models.CharField(choices=[('Digital', 'Digital'), ('Analogue', 'Analogue'), ('Automatic', 'Automatic'), ('Pilot', 'Pilot'), ('Chronograph', 'Chronograph'), ('Diving', 'Diving'), ('Mechanical', 'Mechanical'), ('Smart', 'Smart'), ('Luxury', 'Luxury')], default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='wo_product',
            name='size',
            field=models.CharField(choices=[('M', 'M'), ('L', 'L'), ('one-size', 'one-size'), ('pack', 'pack')], default='', max_length=150),
        ),
    ]
