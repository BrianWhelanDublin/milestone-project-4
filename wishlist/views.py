from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse, HttpResponse)
from stock.models import Item
from django.contrib import messages


def view_wishlist(request):
    ''' a view to show the users wishlist '''

    template = "wishlist/wishlist.html"
    return render(request,
                  template)


def add_to_wishlist(request, item_id):
    if request.method == "POST":
        wishlist = request.session.get("wishlist", {})

        wishlist[item_id] = 1
        request.session["wishlist"] = wishlist
        item = get_object_or_404(Item, pk=item_id)
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

            wishlist = request.session.get("wishlist", {})

            wishlist.pop(item_id)
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
