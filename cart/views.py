from django.shortcuts import render


def view_cart(request):
    ''' A view to show the the cart '''

    template = "cart/cart.html"

    return render(request,
                  template)
