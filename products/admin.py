from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'model', 'price')
    list_filter = ('category', 'model')
    search_fields = ('name', 'model')
