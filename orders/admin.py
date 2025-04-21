from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'order_date', 'status')
    list_filter = ('status', 'order_date')
    search_fields = ('user__username', 'product__name')
