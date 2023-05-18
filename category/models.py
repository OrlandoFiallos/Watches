from django.db import models
from django.utils.text import slugify 
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(verbose_name='Nombre categoría ',max_length=50, unique=True)
    slug = models.SlugField(unique=True, max_length=50)
    category_image = models.ImageField(verbose_name='Imagen categoría',upload_to='photos/categories',blank=True)
    
    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
    
    def __str__(self) -> str:
        return self.category_name

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])