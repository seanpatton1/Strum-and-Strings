from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse
from products.models import Product
from .models import CartItem
from decimal import Decimal
from orders.models import Order, OrderItem
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

    # ✅ Handle form submission (POST)
    if request.method == 'POST':
        request.session['checkout_data'] = {
            'full_name': request.POST.get('full_name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'street_address1': request.POST.get('street_address1'),
            'street_address2': request.POST.get('street_address2'),
            'country': request.POST.get('country'),
            'postal_code': request.POST.get('postal_code'),
            'town_or_city': request.POST.get('town_or_city'),
        }
        return redirect('cart:success')

    return render(request, 'cart/checkout.html', {
        'cart_items': cart_items,
        'total': total,
        'delivery_fee': delivery_fee,
        'grand_total': grand_total,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
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

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url='http://127.0.0.1:8000/cart/success/',
            cancel_url='http://127.0.0.1:8000/cart/',
        )

        return JsonResponse({'id': session.id})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@login_required
def success(request):
    # Get cart items
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        return redirect('products:products_list')

    # Load session form data
    checkout_data = request.session.get('checkout_data', {})

    # Calculate totals
    total = sum(item.product.price * item.quantity for item in cart_items)
    free_delivery_threshold = Decimal('50.00')
    delivery_fee = Decimal('0.00') if total >= free_delivery_threshold else Decimal('4.95')
    grand_total = total + delivery_fee

    # Create Order with real user input
    order = Order.objects.create(
        user=request.user,
        full_name=checkout_data.get('full_name'),
        email=checkout_data.get('email'),
        phone=checkout_data.get('phone'),
        street_address1=checkout_data.get('street_address1'),
        street_address2=checkout_data.get('street_address2'),
        country=checkout_data.get('country'),
        postal_code=checkout_data.get('postal_code'),
        town_or_city=checkout_data.get('town_or_city'),
        delivery_fee=delivery_fee,
        order_total=total,
        grand_total=grand_total,
        status='processing'
    )

    # Create OrderItems
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    # Clear cart
    cart_items.delete()

    # Clear session form data
    request.session.pop('checkout_data', None)

    return render(request, 'cart/success.html', {'order': order})
