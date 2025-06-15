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
    path('admin-dashboard/catalog/', views.product_catalog, name='product_catalog'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
    path('admin-dashboard/orders/', views.order_list, name='admin_order_list'),
    path('admin-dashboard/orders/<int:order_id>/edit/', views.admin_edit_order, name='admin_edit_order'),
    path("newsletter/save-email/", views.save_newsletter_email, name="save_newsletter_email"),
    path('admin-dashboard/products/<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('admin-dashboard/products/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('admin-dashboard/newsletter/', views.newsletter_list, name='newsletter_list'),
    path('admin-dashboard/newsletter/<int:subscriber_id>/edit/', views.newsletter_update, name='newsletter_update'),
    path('newsletter/success/', views.newsletter_success, name='newsletter_success'),
    path('admin-dashboard/newsletter/<int:subscriber_id>/delete/', views.newsletter_delete, name='newsletter_delete')
]
