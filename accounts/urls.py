from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path(
        'newsletter-signup/',
        views.newsletter_signup,
        name='newsletter_signup'
    ),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/add-product/', views.add_product, name='add_product'),
    path('admin-dashboard/orders/', views.order_list, name='order_list'),
    path('admin-dashboard/catalog/', views.product_catalog, name='product_catalog')
]
