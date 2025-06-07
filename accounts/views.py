from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import UserProfile
from .forms import ProfileForm, NewsletterSignupForm
from orders.models import Order
from products.forms import ProductForm


@staff_member_required
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')


@staff_member_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully.')
            return redirect('accounts:add_product')
    else:
        form = ProductForm()

    return render(request, 'accounts/add_product.html', {'form': form})


@staff_member_required
def order_list(request):
    return render(request, 'accounts/order_list.html')


@staff_member_required
def product_catalog(request):
    return render(request, 'accounts/product_catalog.html')


@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )
    orders = Order.objects.filter(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your profile has been updated successfully!"
            )
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'accounts/profile.html', {
        'form': form,
        'orders': orders,  # Pass orders to the template
    })


def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Thank you for subscribing to our newsletter!'
            )
            return redirect('home')
    else:
        form = NewsletterSignupForm()
    return render(request, 'accounts/newsletter_signup.html', {'form': form})
