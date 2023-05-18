from .models import Category

def category_processor(request):
    categories = Category.objects.all().order_by('category_name')
    return {
        'categories':categories
    }