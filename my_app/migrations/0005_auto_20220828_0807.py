# Generated by Django 2.2.2 on 2022-08-28 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_auto_20220828_0629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devotional',
            name='day',
        ),
        migrations.RemoveField(
            model_name='devotional',
            name='month',
        ),
        migrations.RemoveField(
            model_name='devotional',
            name='year',
        ),
    ]