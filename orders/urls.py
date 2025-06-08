from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    path('cancel/<int:order_id>/', views.cancel_order, name='cancel_order')
]
