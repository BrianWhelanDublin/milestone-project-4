from django.conf import settings


def cart_contents(request):

    ''' Creates the cart contents context to be used
    throughout the site not just in the cart app '''

    cart_items = []
    total = 0
    item_count = 0

    home_delivery = settings.STANDARD_HOME_DELIVERY_COST

    subtotal = home_delivery + total

    context = {
        "cart_items": cart_items,
        "total": total,
        "item_count": item_count,
        "home_delivery": home_delivery,
        "subtotal": subtotal,
    }

    return context
