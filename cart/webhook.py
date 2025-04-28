import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .webhook_handler import StripeWH_Handler


@require_POST
@csrf_exempt
def webhook(request):
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=f"Webhook error: {str(e)}", status=400)

    # Set up a webhook handler
    handler = StripeWH_Handler(request)

    # Map webhook events to handler functions
    event_map = {
        'checkout.session.completed':
        handler.handle_checkout_session_completed,
    }

    # Get the event type from Stripe
    event_type = event['type']

    # If there is a handler, use it, else use the generic one
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the handler with the event
    response = event_handler(event)
    return response
