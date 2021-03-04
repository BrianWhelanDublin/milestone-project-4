from django.shortcuts import (render, redirect,
                              get_object_or_404, reverse,
                              HttpResponse)
from stock.models import Item


def view_cart(request):
    ''' A view to show the the cart '''

    template = "cart/cart.html"

    return render(request,
                  template)


def add_to_cart(request, item_id):
    ''' A view to add items to the cart '''

    item = get_object_or_404(Item, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")

    cart = request.session.get("cart", {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session["cart"] = cart
    print(request.session["cart"])
    return redirect(redirect_url)


def update_cart(request, item_id):
    ''' View to update the cart when the quantity has changed '''

    item = get_object_or_404(Item, pk=item_id)
    quantity = int(request.POST.get("item_quantity"))

    cart = request.session.get("cart", {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session["cart"] = cart

    return redirect(reverse("view_cart"))


def remove_from_cart(request, item_id):
    ''' View to remove items from the cart '''
    try:
        item = get_object_or_404(Item, pk=item_id)

        cart = request.session.get("cart", {})

        cart.pop(item_id)

        request.session["cart"] = cart
        return HttpResponse(status=200)

    except Exception as e:

        return HttpResponse(status=500)
