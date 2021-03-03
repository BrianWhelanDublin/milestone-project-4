from django.shortcuts import render, redirect


def view_cart(request):
    ''' A view to show the the cart '''

    template = "cart/cart.html"

    return render(request,
                  template)


def add_to_cart(request, item_id):
    ''' A view to add items to the cart '''

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
