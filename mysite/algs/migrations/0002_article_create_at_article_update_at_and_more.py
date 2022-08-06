# Generated by Django 4.1 on 2022-08-06 13:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 8, 6, 16, 1, 24, 450996)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='publicated',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
    ]
