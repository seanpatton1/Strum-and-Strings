from django.shortcuts import render
from .models import Category


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories_list.html', {
        'categories': categories
    })
