# Generated by Django 2.2 on 2019-04-25 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0003_payment_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.CharField(default='', max_length=50)),
                ('product_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='men.product')),
            ],
        ),
    ]