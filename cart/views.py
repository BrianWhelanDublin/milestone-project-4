from django.shortcuts import (render, redirect,
                              get_object_or_404, reverse,
                              HttpResponse)
from django.contrib import messages
from stock.models import Item


def view_cart(request):
    ''' A view to show the the cart '''

    template = "cart/cart.html"

    return render(request,
                  template)


def add_to_cart(request, item_id):
    ''' A view to add items to the cart. It also
    throws an error message and redirects to the
    homepage if a user tries to type the url into the browser'''

    if request.method == "POST":
        item = get_object_or_404(Item, pk=item_id)
        quantity = int(request.POST.get("quantity"))
        redirect_url = request.POST.get("redirect_url")

        cart = request.session.get("cart", {})

        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request,
                             f"{item.name}'s \
quantity has been updated to {cart[item_id]}", extra_tags="show_items")
        else:
            cart[item_id] = quantity
            messages.success(request,
                             f"{item.name} \
has been added to your cart.", extra_tags="show_items")

        request.session["cart"] = cart

        return redirect(redirect_url)
    else:
        messages.error(request, "Error you do not have permission to do this.")
        return redirect(reverse("home_page"))


def update_cart(request, item_id):
    ''' View to update the cart when the quantity has changed.
    It also throws an error message if a user tries
    to type the url into the browser '''

    if request.method == "POST":
        item = get_object_or_404(Item, pk=item_id)
        quantity = int(request.POST.get("item_quantity"))

        cart = request.session.get("cart", {})

        if quantity > 0:
            cart[item_id] = quantity
            # code from stack overflow to add
            # extra tags to messages details in readme
            messages.success(request,
                             f"{item.name}'s \
 quantity has been updated to {cart[item_id]}", extra_tags="show_items")
        else:
            cart.pop(item_id)
            messages.success(request,
                             f"{item.name} has been removed from your cart.",
                             extra_tags="show_items")

        request.session["cart"] = cart

        return redirect(reverse("view_cart"))
    else:
        messages.error(request, "Error you do not have permission to do this.")
        return redirect(reverse("home_page"))


def remove_from_cart(request, item_id):
    ''' View to remove items from the cart.
     It also throws an error message if a user tries
    to type the url into the browser'''

    if request.method == "POST":
        try:
            item = get_object_or_404(Item, pk=item_id)

            cart = request.session.get("cart", {})

            cart.pop(item_id)
            messages.success(request,
                             f"{item.name} has been removed from your cart.",
                             extra_tags="show_items")

            request.session["cart"] = cart
            return HttpResponse(status=200)

        except Exception as error:
            messages.error(request, f"Error removing item {error}")
            return HttpResponse(status=500)
    else:
        messages.error(request, "Error you do not have permission to do this.")
        return redirect(reverse("home_page"))
