# Generated by Django 3.1.1 on 2020-09-20 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200920_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]