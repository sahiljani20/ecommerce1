# Generated by Django 2.1.4 on 2019-04-14 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Subject', models.CharField(max_length=250)),
                ('Message', models.CharField(max_length=50)),
            ],
        ),
    ]
