from django.shortcuts import render, redirect, get_object_or_404
from category.models import Category
from .models import Product, ProductGallery
from django.db.models import Q 
#paginator
from django.core.paginator import Paginator

def products_by_category(request, category_slug):
    # is_empty = False
    # product_count = 0
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        
        if 'keyword' in request.GET:
            keyword = request.GET['keyword']
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            paginator = Paginator(products, 3)
            page = request.GET.get('page')
            paged_products = paginator.get_page(page)
            product_count = products.count()
        else:
            products = Product.objects.filter(category=category, is_available=True)
            paginator = Paginator(products, 3)
            page = request.GET.get('page')
            paged_products = paginator.get_page(page)
            product_count = products.count()
    else:
        products = Product.objects.filter(is_available=True).order_by('id')
        paginator = Paginator(products,3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    context = {
        'category':category,
        'products': paged_products,
        'product_count': product_count,
    }
    
    return render(request, 'store/products_by_category.html', context)
        
def product_detail(request, category_slug, product_slug):

    product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    features = product.caracteristicas.all()
    product_gallery = ProductGallery.objects.filter(product=product)
    
    
    context = {
        'product':product,
        'features':features,
        'product_gallery':product_gallery,
    }
    
    return render(request, 'store/product_detail.html', context)

def buy(request):
    return render(request, 'store/comprar.html')

def store(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        products = Product.objects.order_by('product_name').filter(Q(description__icontains=keyword) | Q (product_name__icontains=keyword))
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all()
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    
    context = {
        'products':paged_products,
        'product_count':product_count,
    }
    
    return render(request, 'store/store.html', context)