from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm


def checkout(request):
    ''' a view for the checkout page '''

    cart = request.session.get("cart", {})
    if not cart:
        messages.error(request, "Your cart is currently empty.")
        return redirect(reverse("all_items"))

    order_form = OrderForm()
    template = "checkout/checkout.html"

    context = {
        "form": order_form,
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY
    }

    return render(request,
                  template,
                  context)
