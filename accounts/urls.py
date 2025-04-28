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
]
