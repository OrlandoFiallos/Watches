from django.urls import path
from . import views

urlpatterns = [
    path('product-category/<slug:category_slug>', views.products_by_category, name='products_by_category'),
    path('product/<slug:category_slug>/<slug:product_slug>', views.product_detail, name='product_detail'),
    path('comprar/', views.buy, name='buy'),
    path('', views.store, name='store'),
]