from decimal import Decimal
from django.shortcuts import render, get_object_or_404
from .models import Product, Brand
from categories.models import Category
from django.db.models import Q
from random import sample


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # Get related products from the same category (excluding current product)
    related_products = Product.objects.filter(
        category=product.category
    ).exclude(id=product.id)

    # Randomly pick up to 4 related products
    related_products = sample(
                    list(related_products),
                    min(len(related_products), 4)
                )

    return render(request, 'products/product_details.html', {
        'product': product,
        'related_products': related_products,
    })


def products_list(request):
    products = Product.objects.all()

    # 1) Search query
    query = request.GET.get('q')
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(short_description__icontains=query)
        )

    # 2) Category filter
    category_filter = request.GET.get('category')
    if category_filter:
        products = products.filter(category__pk=category_filter)

    # 3) Brand filter
    brand_filter = request.GET.get('brand')
    if brand_filter:
        products = products.filter(brand=brand_filter)

    # 4) Price filter
    price_filter = request.GET.get('price')
    price_ranges = {
        'under200':  (None,                 Decimal('200.00')),
        '200-500':   (Decimal('200.00'),    Decimal('500.00')),
        '500-1000':  (Decimal('500.00'),    Decimal('1000.00')),
        'over1000':  (Decimal('1000.00'),   None),
    }
    if price_filter in price_ranges:
        lower, upper = price_ranges[price_filter]
        if lower is not None:
            products = products.filter(price__gte=lower)
        if upper is not None:
            products = products.filter(price__lte=upper)

    # Sidebar choices
    categories = Category.objects.all()
    brands = Brand.objects.filter(products__in=products).distinct().order_by("name")

    return render(request, 'products/products_list.html', {
        'products':          products,
        'categories':        categories,
        'brands':            brands,
        'selected_category': category_filter,
        'selected_brand':    brand_filter,
        'price_filter':      price_filter,
        'query':             query,
    })
