from django.db import models
from django.urls import reverse

from autoslug.fields import AutoSlugField


# Модель статьи
class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название статьи')
    slug = AutoSlugField(populate_from='title', verbose_name='URL')
    photo = models.ImageField(upload_to='%Y/%m/%d', verbose_name='Лого')
    content = models.TextField(verbose_name='Содержимое статьи')
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, verbose_name='Категория')
    publicated = models.BooleanField(default=True, verbose_name='Опубликовано')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Отредактировано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', kwargs={'cat_slug': self.category.slug, 'article_slug': self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-id', 'title']


# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')
    slug = AutoSlugField(populate_from='name', verbose_name='URL')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-id', 'name']


# Модель заметок
class Note(models.Model):
    OPTIONS = [
        ("add", "Дополнение"),
    ]

    article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name='Статья')
    name = models.CharField(max_length=125, verbose_name='Название заметки')
    type = models.CharField(max_length=50, choices=OPTIONS, default=OPTIONS[0][0], verbose_name='Тип заметки')
    content = models.TextField(verbose_name='Содержимое заметки')

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['-id', 'article']
