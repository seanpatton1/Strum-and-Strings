from decimal import Decimal

from django.shortcuts import render, get_object_or_404

from .models import Category
from products.models import Product


def categories_list(request):
    """
    Show all categories.
    """
    categories = Category.objects.all()
    return render(request, 'categories/categories_list.html', {
        'categories': categories
    })


def category_detail(request, pk):
    """
    Display a category page with optional filtering
    by model, brand, and price ranges.
    """
    category = get_object_or_404(Category, pk=pk)

    # keep an unfiltered copy for the sidebar
    all_products = Product.objects.filter(category=category)
    # start with all products, then apply any filters
    products = all_products

    # Model filter
    model_filter = request.GET.get('model')
    if model_filter:
        products = products.filter(model=model_filter)

    # Brand filter
    brand_filter = request.GET.get('brand')
    if brand_filter:
        products = products.filter(brand=brand_filter)

    # Price‑range filter (keys must match your template links)
    price_filter = request.GET.get('price')
    price_ranges = {
        'under200':    (None,                Decimal('200.00')),
        '200-500':     (Decimal('200.00'),   Decimal('500.00')),
        '500-1000':    (Decimal('500.00'),   Decimal('1000.00')),
        'over1000':    (Decimal('1000.00'),  None),
    }
    if price_filter in price_ranges:
        lower, upper = price_ranges[price_filter]
        if lower is not None:
            products = products.filter(price__gte=lower)
        if upper is not None:
            products = products.filter(price__lte=upper)

    # Sidebar lists always drawn from the unfiltered set
    models = (
        all_products
        .values_list('model', flat=True)
        .distinct()
        .order_by('model')
    )
    brands = (
        all_products
        .values_list('brand', flat=True)
        .distinct()
        .order_by('brand')
    )

    context = {
        'category':     category,
        'products':     products,
        'models':       models,
        'brands':       brands,
        'model_filter': model_filter,
        'brand_filter': brand_filter,
        'price_filter': price_filter,
    }
    return render(request, 'categories/category_detail.html', context)


def product_detail(request, pk):
    """
    Display a single Product’s details.
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {
        'product': product
    })
