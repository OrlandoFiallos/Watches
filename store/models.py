from django.db import models
from django.urls import reverse
from category.models import Category

class ProductFeature(models.Model):
    # producto = models.ManyToManyField(Product, related_name='productos')
    caracteristica = models.CharField(verbose_name='Característica',max_length=100)
    
    class Meta:
        verbose_name = 'Característica del producto'
        verbose_name_plural = 'Carecterísticas del producto'
    
    def __str__(self) -> str:
        return self.caracteristica

class Product(models.Model):
    product_name = models.CharField(verbose_name='Nombre del producto',max_length=200, unique=True)
    caracteristicas = models.ManyToManyField(ProductFeature)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(verbose_name='Descripción',max_length=100, blank=True)
    price = models.IntegerField(verbose_name='Precio')
    images = models.ImageField(verbose_name='Imagen producto',upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Categoría')
    created_date = models.DateTimeField(verbose_name='Fecha creación',auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name='Fecha modificacón',auto_now=True)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self) -> str:
        return self.product_name
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/products', max_length=255)
    
    class Meta:
        verbose_name = 'Galería de producto'
        verbose_name_plural = 'Galería de productos'
    
    def __str__(self) -> str:
        return self.product.product_name

