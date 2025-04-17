from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, pk):
    """
    View to display a single Product’s details.
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {
        'product': product
    })
