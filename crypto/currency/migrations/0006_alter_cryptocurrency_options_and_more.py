# Generated by Django 4.0.5 on 2022-07-04 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0005_category_cryptocurrency_cat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cryptocurrency',
            options={'ordering': ['name'], 'verbose_name': 'Криптовалюты', 'verbose_name_plural': 'Криптовалюты'},
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='images/currency/'),
        ),
    ]
