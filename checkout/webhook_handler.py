from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from stock.models import Item
from users.models import UserProfile

import json
import time


class StripeWebhookHandler:
    ''' Class to handle strip webhooks '''

    def __init__(self, request):
        self.request = request

    def _send_order_confirmation(self, order):
        ''' send the confirmation email to the user '''
        users_email = order.email
        subject = render_to_string(
            "checkout/email_confirmation/confirmation_subject.txt",
            {"order": order})
        body = render_to_string(
            "checkout/email_confirmation/confirmation_body.txt",
            {"order": order,
             "contact_email": settings.DEFAULT_EMAIL_ADDRESS
             })

        send_mail(
            subject,
            body,
            settings.DEFAULT_EMAIL_ADDRESS,
            [users_email]
        )

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
        ''' handles a suceeded payment intent webhook from stripe '''
        intent = event.data.object

        payment_intent_id = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        delivery_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount/100, 2)

        for field, value in delivery_details.address.items():
            if value == "":
                delivery_details.address[field] = None

        user_profile = None
        username = intent.metadata.username
        if username != "AnonymousUser":
            user_profile = UserProfile.objects.get(
                user__username=username)
            if save_info:
                user_profile.user_contact_number = delivery_details.phone
                user_profile.user_street_address_1 = \
                    delivery_details.address.line1
                user_profile.user_street_address_2 = \
                    delivery_details.address.line2
                user_profile.user_town_or_city = \
                    delivery_details.address.city,
                user_profile.user_county = delivery_details.address.state
                user_profile.user_eircode = \
                    delivery_details.address.postal_code
                user_profile.user_country = delivery_details.address.country
                user_profile.save()

        order_exists = False
        attempt = 1

        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=delivery_details.name,
                    email__iexact=billing_details.email,
                    contact_number__iexact=delivery_details.phone,
                    street_address_1__iexact=delivery_details.address.line1,
                    street_address_2__iexact=delivery_details.address.line2,
                    town_or_city__iexact=delivery_details.address.city,
                    county__iexact=delivery_details.address.state,
                    eircode__iexact=delivery_details.address.postal_code,
                    country__iexact=delivery_details.address.country,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_payment_intent_id=payment_intent_id,
                )
                order_exists = True
                break

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            self._send_order_confirmation(order)
            return HttpResponse(
                    content=f"Webhook recieved : {event['type']} | SUCCESS: \
Verified order is in database.", status=200)

        else:
            order = None
            try:
                order = Order.objects.create(
                        full_name=delivery_details.name,
                        user_profile=user_profile,
                        email=billing_details.email,
                        contact_number=delivery_details.phone,
                        street_address_1=delivery_details.address.line1,
                        street_address_2=delivery_details.address.line2,
                        town_or_city=delivery_details.address.city,
                        county=delivery_details.address.state,
                        eircode=delivery_details.address.postal_code,
                        country=delivery_details.address.country,
                        grand_total=grand_total,
                        original_cart=cart,
                        stripe_payment_intent_id=payment_intent_id,
                    )
                for item_id, quantity in json.loads(cart).items():
                    item = Item.objects.get(id=item_id)
                # cretes the line items
                    order_line_item = OrderLineItem(
                        order=order,
                        item=item,
                        quantity=quantity,
                        )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content="Webhook recieved \
: {event['type']} | ERROR : {e}", status=500)

        self._send_order_confirmation(order)
        return HttpResponse(
            content=f"Webhook recieved : {event['type']} | \
 SUCCESS: Created order in webhook", status=200)
