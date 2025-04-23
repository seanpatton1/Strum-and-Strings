from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import CartItem
from orders.models import Order, OrderItem
from decimal import Decimal


class StripeWH_Handler:
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}",
            status=200
        )

    def handle_checkout_session_completed(self, event):
        print("Webhook: checkout.session.completed received")

        session = event['data']['object']
        metadata = session.get('metadata', {})
        print("Metadata received in webhook:", metadata)

        username = metadata.get('username')

        if not username:
            print("No username in metadata. Skipping order creation.")
            return HttpResponse(content="Webhook received with no username metadata.", status=200)

        try:
            user = User.objects.get(username=username)
            cart_items = CartItem.objects.filter(user=user)

            total = sum(item.product.price * item.quantity for item in cart_items)
            free_delivery_threshold = Decimal('50.00')
            delivery_fee = Decimal('0.00') if total >= free_delivery_threshold else Decimal('4.95')
            grand_total = total + delivery_fee

            checkout_data = {
                            'full_name': metadata.get('full_name'),
                            'email': metadata.get('email'),
                            'phone': metadata.get('phone'),
                            'street_address1': metadata.get('street_address1'),
                            'street_address2': metadata.get('street_address2'),
                            'country': metadata.get('country'),
                            'postal_code': metadata.get('postal_code'),
                            'town_or_city': metadata.get('town_or_city'),
                            }

            order = Order.objects.create(
                user=user,
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
                stripe_session_id=session.get('id'),
                status='processing'
            )

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )

            cart_items.delete()

            return HttpResponse(content="Order created via webhook.", status=200)

        except Exception as e:
            print(f"Webhook error: {e}")
            return HttpResponse(content=f"Webhook order creation failed: {str(e)}", status=500)
