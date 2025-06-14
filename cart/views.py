from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse
from products.models import Product
from .forms import CheckoutForm
from .models import CartItem
from decimal import Decimal
from django.contrib import messages
from orders.models import Order
from accounts.models import UserProfile
from django.views.decorators.http import require_POST
import stripe
import json


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER', 'products:products_list'))


@require_POST
@login_required
def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)

    try:
        quantity = int(request.POST.get('quantity'))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    except (ValueError, TypeError):
        pass

    return redirect('cart:view_cart')


@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)

    for item in cart_items:
        item.subtotal = item.product.price * item.quantity

    total = sum(item.subtotal for item in cart_items)

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total': total,
    })


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('cart:view_cart')


@login_required
def delete_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart:view_cart')


@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)

    for item in cart_items:
        item.subtotal = item.product.price * item.quantity

    total = sum(item.subtotal for item in cart_items)

    # Delivery logic
    delivery_fee = Decimal('0.00')
    free_delivery_threshold = Decimal('50.00')

    if total < free_delivery_threshold:
        delivery_fee = Decimal('4.95')

    grand_total = total + delivery_fee

    # Pre-populate profile data
    initial_data = {}
    try:
        profile = request.user.userprofile
        initial_data = {
            'first_name': f"{request.user.first_name}",
            'last_name': f"{request.user.last_name}",
            'email': request.user.email,
            'phone': profile.phone,
            'street_address1': profile.address,
            'street_address2': '',
            'country': profile.country,
            'postal_code': profile.postcode,
            'town_or_city': profile.city,
        }
    except UserProfile.DoesNotExist:
        pass

    # Handle form submission (POST)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Store form data in session or process as needed
            request.session['checkout_data'] = form.cleaned_data
            return redirect('cart:success')
    else:
        form = CheckoutForm(initial=initial_data)

    return render(request, 'cart/checkout.html', {
        'form': form,
        'cart_items': cart_items,
        'total': total,
        'delivery_fee': delivery_fee,
        'grand_total': grand_total,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'profile_data': initial_data,
    })


@require_POST
@login_required
def create_checkout_session(request):
    try:
        data = json.loads(request.body)
        request.session['checkout_data'] = data

        cart_items = CartItem.objects.filter(user=request.user)
        line_items = []
        total = Decimal('0.00')

        for item in cart_items:
            subtotal = item.product.price * item.quantity
            total += subtotal
            line_items.append({
                'price_data': {
                    'currency': 'gbp',
                    'unit_amount': int(item.product.price * 100),
                    'product_data': {
                        'name': item.product.name,
                    },
                },
                'quantity': item.quantity,
            })

        free_delivery_threshold = Decimal('50.00')
        if total < free_delivery_threshold:
            delivery_fee = Decimal('4.95')
            line_items.append({
                'price_data': {
                    'currency': 'gbp',
                    'unit_amount': int(delivery_fee * 100),
                    'product_data': {
                        'name': 'Delivery Fee',
                    },
                },
                'quantity': 1,
            })

        stripe.api_key = settings.STRIPE_SECRET_KEY

        if settings.DEBUG:
            domain = 'http://127.0.0.1:8000'
        else:
            domain = 'https://strum-and-strings-e5017bc28566.herokuapp.com'

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=(
                f'{domain}/cart/success/?session_id={{CHECKOUT_SESSION_ID}}'
            ),
            cancel_url=f'{domain}/cart/checkout/cancel/',
            metadata={
                'username': request.user.username,
                'first_name': data.get('first_name'),
                'last_name': data.get('last_name'),
                'email': data.get('email'),
                'phone': data.get('phone'),
                'street_address1': data.get('street_address1'),
                'street_address2': data.get('street_address2'),
                'country': data.get('country'),
                'postal_code': data.get('postal_code'),
                'town_or_city': data.get('town_or_city'),
            }
        )

        return JsonResponse({'id': session.id})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def success(request):
    session_id = request.GET.get('session_id')

    if not session_id:
        messages.error(request, "No session ID provided.")
        return redirect('products:products_list')

    try:
        # Find order by session_id
        order = Order.objects.get(stripe_session_id=session_id)

        if request.user.is_authenticated and order.user != request.user:
            messages.error(
                request,
                "You are not authorized to view this order."
            )
            return redirect('products:products_list')

        # Clear the cart (only if the user is authenticated)
        if request.user.is_authenticated:
            CartItem.objects.filter(user=request.user).delete()

        order_items = order.items.all()

    except Order.DoesNotExist:
        messages.error(request, "Order not found.")
        return redirect('products:products_list')

    return render(
            request,
            'cart/success.html',
            {
                'order': order,
                'order_items': order_items,
            }
        )


def cancel(request):
    return render(request, 'cart/cancel.html')
