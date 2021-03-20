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

        wishlist[item_id] = item_id
        request.session["wishlist"] = wishlist
        item = get_object_or_404(Item, pk=item_id)
        messages.success(request,
                         f"{item.name} has been added to your wishlist.")
        return HttpResponse(status=200)
    else:
        messages.error(request,
                       "You do not have permission to do this.")
        return redirect(reverse("all_items"))
