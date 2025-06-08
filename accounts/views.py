from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import UserProfile, NewsletterSubscriber
from .forms import ProfileForm, NewsletterSignupForm, OrderStatusForm
from orders.models import Order
from products.forms import ProductForm


@staff_member_required
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')


@staff_member_required
def admin_edit_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    if request.method == 'POST':
        form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('accounts:admin_order_detail', order_id=order.id)
    else:
        form = OrderStatusForm(instance=order)

    return render(request, 'accounts/admin_edit_order.html', {
        'form': form,
        'order': order,
    })


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
    orders = Order.objects.select_related('user').order_by('-created_at')
    return render(request, 'accounts/order_list.html', {
        'orders': orders
    })


@staff_member_required
def product_catalog(request):
    return render(request, 'accounts/product_catalog.html')


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    form = OrderStatusForm(request.POST or None, instance=order)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('accounts:admin_order_detail', order_id=order.id)

    return render(request, 'accounts/admin_order_detail.html', {
        'order': order,
        'form': form
    })


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


@csrf_exempt
def save_newsletter_email(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = request.user if request.user.is_authenticated else None

        if email:
            # Either get existing or create new entry
            subscriber, created = NewsletterSubscriber.objects.get_or_create(
                email=email,
                defaults={'user': user}
            )
            # If it exists but user was not saved before, update it
            if not subscriber.user and user:
                subscriber.user = user
                subscriber.save()

            return JsonResponse({"status": "success"})

    return JsonResponse({"status": "error"}, status=400)