from django.http import HttpResponse
from django.contrib.auth.models import User
from decimal import Decimal
from .models import CartItem
from orders.models import Order, OrderItem
import logging


logger = logging.getLogger(__name__)


class StripeWH_Handler:
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}",
            status=200
        )

    def handle_checkout_session_completed(self, event):
        session = event['data']['object']
        metadata = session.get('metadata', {})

        username = metadata.get('username')
        if not username:
            logger.warning("Webhook received but no username in metadata.")
            return HttpResponse(
                content="Webhook received with no username metadata.",
                status=200
            )

        try:
            user = User.objects.get(username=username)
            cart_items = CartItem.objects.filter(user=user)

            total = sum(
                item.product.price * item.quantity
                for item in cart_items
            )
            free_delivery_threshold = Decimal('50.00')
            delivery_fee = (
                Decimal('0.00')
                if total >= free_delivery_threshold
                else Decimal('4.95')
            )
            grand_total = total + delivery_fee
            # debugging print statement
            print("Creating order for user:", user)

            order = Order.objects.create(
                user=user,
                first_name=metadata.get('first_name'),
                last_name=metadata.get('last_name'),
                email=metadata.get('email'),
                phone=metadata.get('phone'),
                street_address1=metadata.get('street_address1'),
                street_address2=metadata.get('street_address2'),
                country=metadata.get('country'),
                postal_code=metadata.get('postal_code'),
                town_or_city=metadata.get('town_or_city'),
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

            return HttpResponse(
                content="Order created via webhook.",
                status=200
            )

        except Exception as e:
            logger.error(
                f"Error creating order from webhook: {str(e)}",
                exc_info=True
            )
            print("WEBHOOK ORDER ERROR:", str(e))
            return HttpResponse(
                content="Webhook received but error occurred.",
                status=200
            )
