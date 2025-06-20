from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import UserProfile, NewsletterSubscriber
from .forms import ProfileForm, NewsletterSignupForm
from orders.models import Order
from products.models import Product
from products.forms import ProductForm
from accounts.forms import AdminOrderForm


@staff_member_required
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')


@staff_member_required
def admin_edit_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    if request.method == 'POST':
        form = AdminOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('accounts:admin_order_detail', order_id=order.id)
    else:
        form = AdminOrderForm(instance=order)

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
    categories = ['Acoustic', 'Electric', 'Accessories']
    paginated_products = {}

    for category in categories:

        products = Product.objects.filter(category__name=category)

        paginator = Paginator(products, 5)

        page_number = request.GET.get(f'page_{category}', 1)
        page_obj = paginator.get_page(page_number)

        paginated_products[category] = page_obj

    return render(request, 'accounts/product_catalog.html', {
        'categories': categories,
        'paginated_products': paginated_products,
    })


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    form = AdminOrderForm(request.POST or None, instance=order)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('accounts:admin_order_detail', order_id=order.id)

    return render(request, 'accounts/admin_order_detail.html', {
        'order': order,
        'form': form
    })


@staff_member_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect('accounts:product_catalog')
    else:
        form = ProductForm(instance=product)

    return render(request, 'accounts/edit_product.html', {
        'form': form,
        'product': product
    })


@staff_member_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('accounts:product_catalog')

    return render(request, 'accounts/confirm_delete_product.html', {
        'product': product
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


@staff_member_required
def newsletter_list(request):
    subscribers = NewsletterSubscriber.objects.all()
    return render(
        request,
        'accounts/newsletter_list.html',
        {'subscribers': subscribers}
    )


@staff_member_required
def newsletter_update(request, subscriber_id):
    subscriber = get_object_or_404(NewsletterSubscriber, id=subscriber_id)
    form = NewsletterSignupForm(request.POST or None, instance=subscriber)

    if form.is_valid():
        form.save()
        messages.success(request, 'Subscriber updated successfully.')
        return redirect('accounts:newsletter_list')

    return render(request, 'accounts/newsletter_form.html', {
        'form': form,
        'title': 'Edit Subscriber',
    })


@staff_member_required
def newsletter_delete(request, subscriber_id):
    subscriber = get_object_or_404(NewsletterSubscriber, id=subscriber_id)

    if request.method == 'POST':
        subscriber.delete()
        messages.success(request, 'Subscriber deleted successfully.')
        return redirect('accounts:newsletter_list')

    return render(request, 'accounts/newsletter_confirm_delete.html', {
        'subscriber': subscriber
    })


def newsletter_success(request):
    return render(request, 'accounts/newsletter_success.html')


@require_POST
@csrf_exempt
def check_newsletter_email(request):
    email = request.POST.get('email')
    if email:
        exists = NewsletterSubscriber.objects.filter(email=email).exists()
        return JsonResponse({'subscribed': exists})
    return JsonResponse({'error': 'No email provided'}, status=400)
