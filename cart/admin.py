from django.contrib import admin
from .models import CartItem


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'added_on')
    list_filter = ('user', 'product')
    search_fields = ('user__username', 'product__name')
