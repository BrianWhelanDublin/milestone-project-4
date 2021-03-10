from django.http import HttpResponse


class StripeWebhookHandler:
    ''' Class to handle strip webhooks '''

    def __init__(self, request):
        self.request = request

    def handle_stripe_event(self, event):
        ''' takes the stripe event and returns a
         http response to indicate its been recieved '''
        return HttpResponse(
            content=f"Unhandled webhook recieved : {event['type']}",
            status=200
            )

    def handle_payment_intent_failed(self, event):
        ''' handles a failed payment intent '''

        return HttpResponse(
            content=f"Webhook recieved : {event['type']}",
            status=200
            )

    def handle_payment_intent_succeded(self, event):
        ''' handles a suceeded payment intent from stripe '''

        return HttpResponse(
            content=f"Webhook recieved : {event['type']}",
            status=200
            )
