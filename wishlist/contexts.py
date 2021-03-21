from django.shortcuts import get_object_or_404
from .models import UsersWishlist


def wishlist_items(request):
    wishlist_items = []
    if request.user.is_authenticated:
        wishlist = get_object_or_404(UsersWishlist, user=request.user)
        wishlist_items = wishlist.items.all()

    context = {
        "wishlist_items": wishlist_items,
    }

    return context
