from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWebhookHandler

import stripe


@require_POST
@csrf_exempt
def webhook(request):
    ''' listens for stripe webhooks code from stripe thats been edited '''

    webhook_secret = settings.STRIPE_WEBHOOK_SECRET
    stripe_api_key = settings.STRIPE_SECRET_KEY

    # gets webhook data and verifies the signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(payload,
                                               sig_header,
                                               webhook_secret)
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # setting up the webhook handler
    handler = StripeWebhookHandler(request)

    # then map the events to relevant functions
    webhook_event_map = {
        "payment_intent.succeeded": handler.handle_payment_intent_succeded,
        "payment_intent.payment_failed": handler.handle_payment_intent_failed,
    }

    # get the event type from stripe
    webhook_event_type = event["type"]

    #  uses the handle_stripe_event by default and if
    #  theres a specific handler it gets it from the map
    webhook_event_handler = webhook_event_map.get(webhook_event_type,
                                                  handler.handle_stripe_event)

    response = webhook_event_handler(event)
    return response
