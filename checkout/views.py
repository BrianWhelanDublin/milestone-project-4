from django.shortcuts import render, redirect, reverse
from django.contrib import messages

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
    }

    return render(request,
                  template,
                  context)
