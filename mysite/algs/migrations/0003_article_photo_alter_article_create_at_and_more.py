# Generated by Django 4.1 on 2022-08-06 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algs', '0002_article_create_at_article_update_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ImageField(default=None, upload_to='%Y/%m/%d', verbose_name='Лого'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создано'),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Отредактировано'),
        ),
    ]
