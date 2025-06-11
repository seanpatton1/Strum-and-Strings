from django.contrib import admin
from .models import Product, Brand


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'model', 'price')
    list_filter = ('category', 'model')
    search_fields = ('name', 'model')
    fields = (
        'name',
        'brand',
        'category',
        'model',
        'id',
        'image',
        'short_description',
        'price',
    )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)
    fields = ('name',)