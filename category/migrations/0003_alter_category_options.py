# Generated by Django 4.2.1 on 2023-05-10 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_category_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'categoría', 'verbose_name_plural': 'categorías'},
        ),
    ]
