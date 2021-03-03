from django.conf import settings
from django.shortcuts import get_object_or_404
from stock.models import Item


def cart_contents(request):

    ''' Creates the cart contents context to be used
    throughout the site not just in the cart app '''

    cart_items = []
    total = 0
    item_count = 0

    cart = request.session.get("cart", {})

    for item_id, quantity in cart.items():
        item = get_object_or_404(Item, pk=item_id)
        total += quantity * item.price
        cart_items.append({
            "item_id": item_id,
            "quantity": quantity,
            "item": item,
        })

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
