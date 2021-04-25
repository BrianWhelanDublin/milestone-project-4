from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse, HttpResponse)
from django.contrib import messages

from .models import UsersWishlist
from stock.models import Item


def view_wishlist(request):
    ''' a view to show the users wishlist '''

    template = "wishlist/wishlist.html"
    return render(request,
                  template)


def add_to_wishlist(request, item_id):
    ''' A view to add an item to the wishlist '''

    if request.method == "POST":
        item = get_object_or_404(Item, pk=item_id)
        wishlist = get_object_or_404(UsersWishlist, user=request.user)
        if item not in wishlist.items.all():
            wishlist.items.add(item)
            messages.success(request,
                             f"{item.name} has been added to your wishlist.")
            return HttpResponse(status=200)
    else:
        messages.error(request,
                       "You do not have permission to do this.")
        return redirect(reverse("all_items"))


def remove_from_wishlist(request, item_id):
    ''' View to remove items from the wishlist '''

    if request.method == "POST":
        try:
            item = get_object_or_404(Item, pk=item_id)
            wishlist = get_object_or_404(UsersWishlist, user=request.user)
            print(item)
            print(wishlist)
            if item in wishlist.items.all():
                wishlist.items.remove(item)
            messages.success(request,
                             f"{item.name} has been removed \
 from your wishlist.")
            return HttpResponse(status=200)
        except Exception as error:
            messages.error(request, f"Error removing item {error}")
            return HttpResponse(status=500)
    else:
        messages.error(request, "Error you do not have \
permission to do this.")
        return redirect(reverse("home_page"))


def delete_wishlist(request):
    ''' A view to delete the wishlist '''

    if request.method == "POST":
        wishlist = get_object_or_404(UsersWishlist, user=request.user)
        wishlist.items.clear()
        messages.success(request, "Your wishlist has been deleted.")
        return redirect(reverse("view_wishlist"))
    else:
        messages.error(request, "Error you do not have \
permission to do this.")
        return redirect(reverse("home_page"))
