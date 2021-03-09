from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe


def checkout(request):
    ''' a view for the checkout page '''

    # stripe variables
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY


    cart = request.session.get("cart", {})
    if not cart:
        messages.error(request, "Your cart is currently empty.")
        return redirect(reverse("all_items"))

    # get total for stripe
    current_cart = cart_contents(request)
    cart_total = current_cart["subtotal"]
    stripe_total = round(cart_total * 100)

    # create stripe payment intent
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
    )


    order_form = OrderForm()
    template = "checkout/checkout.html"

    context = {
        "form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render(request,
                  template,
                  context)
