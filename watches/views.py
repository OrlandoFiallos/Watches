from django.shortcuts import render
from store.models import Product
from category.models import Category

def home(request):
    latest_products_added = Product.objects.all().order_by('-created_date')[:5]
    categories = Category.objects.all()
    context = {
        'latest_products':latest_products_added,
        'categories':categories,
    }
    return render(request, 'home.html', context)