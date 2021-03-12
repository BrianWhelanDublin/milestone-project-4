from django.shortcuts import (render, redirect,
                              reverse, get_object_or_404,
                              HttpResponse)
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST

from .forms import OrderForm
from cart.contexts import cart_contents

from stock.models import Item
from .models import Order, OrderLineItem

import stripe
import json


def checkout(request):
    ''' a view for the checkout page '''

    # stripe variables
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        cart = request.session.get("cart", {})
        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "contact_number": request.POST["contact_number"],
            "street_address_1": request.POST["street_address_1"],
            "street_address_2": request.POST["street_address_2"],
            "town_or_city": request.POST["town_or_city"],
            "county": request.POST["county"],
            "eircode": request.POST["eircode"],
            "country": request.POST["country"],
        }
        order_form = OrderForm(form_data)

        # create the order when a valid form is sent
        if order_form.is_valid():
            order = order_form.save(commit=False)
            payment_intent_id = request.POST.get(
                "client_secret").split("_secret")[0]
            order.stripe_payment_intent_id = payment_intent_id
            order.original_cart = json.dumps(cart)
            order.save()

            for item_id, quantity in cart.items():
                try:
                    item = Item.objects.get(id=item_id)
                    # cretes the line items
                    order_line_item = OrderLineItem(
                        order=order,
                        item=item,
                        quantity=quantity,
                        )
                    order_line_item.save()

                # in the case an item isnt found
                except Item.DoesNotExist:
                    messages.error(request, (
                        "The item wasn't found.\
                            Please contact us for assisstance"
                    ))
                    order.delete()
                    return redirect(reverse("view_cart"))

            # save the users info
            request.session["save_info"] = "save-info" in request.POST
            return redirect(reverse("checkout_success",
                                    args=[order.order_number]))
        # otherwise give an error message
        else:
            messages.error(request, "Theres was an error checking out.\
                Please check your details.")

    else:
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


def checkout_success(request, order_number):
    ''' view for when the checkout was successful '''

    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request,
                     "Your order has been processed!")

    if "cart" in request.session:
        del request.session["cart"]

    template = "checkout/checkout_success.html"

    context = {
        "order": order,
        "on_cart_success": True,
    }

    return render(request,
                  template,
                  context)


@require_POST
def cache_checkout_data(request):
    ''' view to cache data when the checkout form is submitted '''
    try:
        payment_intent_id = request.POST.get(
            "client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY

        stripe.PaymentIntent.modify(payment_intent_id, metadata={
            "username": request.user,
            "save_info": request.POST.get("save_info"),
            "cart": json.dumps(request.session.get("cart", {}))
        })

        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, "Sorry your payment \
            can't be proceeed right now. Please try again later.")
        return HttpResponse(content=e, status=400)
