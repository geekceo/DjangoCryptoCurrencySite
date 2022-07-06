from distutils.command.upload import upload
from pyexpat import model
from tabnanny import verbose
from django.db import models

class CryptoCurrency(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    shortname = models.CharField(max_length=20, verbose_name='Краткое название')
    description = models.TextField(blank=True, verbose_name='Описание')
    icon = models.ImageField(upload_to='currency/images/', blank=True, null=True, verbose_name='Иконка')
    #iconpath = models.CharField(max_length=96, verbose_name='Путь к иконке')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self) -> str:
        return f'{self.name}:{self.shortname}'

    class Meta:
        verbose_name = 'Криптовалюты'
        verbose_name_plural = 'Криптовалюты'
        ordering = ['name']

class Category(models.Model):
    name = models.CharField(max_length=96, db_index=True, verbose_name='Название категории')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id']