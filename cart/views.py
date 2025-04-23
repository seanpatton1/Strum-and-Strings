from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse
from products.models import Product
from .models import CartItem
from decimal import Decimal
from django.contrib import messages
from orders.models import Order
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

    # Handle form submission (POST)
    if request.method == 'POST':
        request.session.pop['checkout_data'] = {
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
            success_url='http://127.0.0.1:8000/cart/success/?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='http://127.0.0.1:8000/cart/',
            metadata={
                        'username': request.user.username,
                        'full_name': data.get('full_name'),
                        'email': data.get('email'),
                        'phone': data.get('phone'),
                        'street_address1': data.get('street_address1'),
                        'street_address2': data.get('street_address2'),
                        'country': data.get('country'),
                        'postal_code': data.get('postal_code'),
                        'town_or_city': data.get('town_or_city'), }
        )

        print("Metadata being sent:", session.metadata)

        return JsonResponse({'id': session.id})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@login_required
def success(request):
    session_id = request.GET.get('session_id')

    if not session_id:
        messages.error(request, "No session ID provided.")
        return redirect('products:products_list')

    try:
        order = Order.objects.get(stripe_session_id=session_id, user=request.user)
    except Order.DoesNotExist:
        messages.error(request, "Order not found.")
        return redirect('products:products_list')

    return render(request, 'cart/success.html', {'order': order})
