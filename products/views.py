from django.shortcuts import render, get_object_or_404
from .models import Product
from categories.models import Category


def product_detail(request, pk):
    """
    View to display a single Product’s details.
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_details.html', {
        'product': product
    })


def products_list(request):
    """
    Show all Products, with optional filtering by category or model.
    """
    qs = Product.objects.select_related('category').all()

    # Filter by category if provided
    category_id = request.GET.get('category')
    if category_id:
        qs = qs.filter(category_id=category_id)

    # Filter by model if provided
    model = request.GET.get('model')
    if model:
        qs = qs.filter(model=model)

    # For sidebar controls
    categories = Category.objects.all()
    models = (
        Product.objects
               .values_list('model', flat=True)
               .distinct()
               .order_by('model')
    )

    return render(request, 'products/products_list.html', {
        'products': qs,
        'categories': categories,
        'models': models,
        'selected_category': category_id,
        'selected_model': model,
    })
