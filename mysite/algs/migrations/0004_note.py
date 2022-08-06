# Generated by Django 4.1 on 2022-08-06 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('algs', '0003_article_photo_alter_article_create_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('add', 'Дополнение')], max_length=50)),
                ('content', models.TextField(verbose_name='Содержимое заметки')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='algs.article', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Заметка',
                'verbose_name_plural': 'Заметки',
                'ordering': ['-id', 'article'],
            },
        ),
    ]
