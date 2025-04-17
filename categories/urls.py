from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.categories_list, name='categories_list'),
    path('<int:pk>/', views.category_detail, name='category_detail'),
]
