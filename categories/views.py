from django.shortcuts import render, get_object_or_404
from .models import Category
from products.models import Product


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories_list.html', {
        'categories': categories
    })


def category_detail(request, pk):
    # 1. Fetch the Category or 404
    category = get_object_or_404(Category, pk=pk)
    # 2. All products in that category
    products = Product.objects.filter(category=category)
    # 3. Distinct models for the sidebar
    models = (
        products
        .values_list('model', flat=True)
        .distinct()
        .order_by('model')
    )
    return render(request, 'categories/category_detail.html', {
        'category': category,
        'products': products,
        'models': models,
    })


def product_detail(request, pk):
    """
    Display a single Product’s details.
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {
        'product': product
    })
