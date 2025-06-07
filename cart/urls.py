from django.urls import path
from .webhook import webhook
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path(
            'remove/<int:item_id>/',
            views.remove_from_cart,
            name='remove_from_cart'
        ),
    path(
            'create-checkout-session/',
            views.create_checkout_session,
            name='create_checkout_session'
        ),
    path('success/', views.success, name='success'),
    path('stripe/webhook/', webhook, name='stripe_webhook'),
    path('update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('delete/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),

]
