# Generated by Django 4.2.1 on 2023-05-10 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_productgallery_options_productfeature'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterModelOptions(
            name='productfeature',
            options={'verbose_name': 'Característica del producto', 'verbose_name_plural': 'Carecterísticas del producto'},
        ),
        migrations.AlterModelOptions(
            name='productgallery',
            options={'verbose_name': 'Galería de producto', 'verbose_name_plural': 'Galería de productos'},
        ),
        migrations.RenameField(
            model_name='productfeature',
            old_name='nombre_caracteristica',
            new_name='caracteristica',
        ),
        migrations.RemoveField(
            model_name='productfeature',
            name='producto',
        ),
        migrations.AddField(
            model_name='product',
            name='caracteristicas',
            field=models.ManyToManyField(to='store.productfeature'),
        ),
    ]
