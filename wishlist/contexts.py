from django.shortcuts import get_object_or_404
from stock.models import Item


def wishlist_items(request):

    wishlist_items = []
    wishlist_count = 0
    wishlist = request.session.get("wishlist", {})

    for item_id in wishlist:
        item = get_object_or_404(Item, pk=item_id)
        wishlist_count += 1
        wishlist_items.append({
            "item_id": item_id,
            "item": item,
            })

    context = {
        "wishlist_items": wishlist_items,
        "wishlist_count": wishlist_count,
    }

    return context
