from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from stock.models import Item
from django.contrib import messages


def view_wishlist(request):
    ''' a view to show the users wishlist '''

    wishlist_items = []
    wishlist = request.session.get("wishlist", {})

    for item_id in wishlist:
        item = get_object_or_404(Item, pk=item_id)
        wishlist_items.append({"item": item})

    template = "wishlist/wishlist.html"
    print(wishlist_items)
    context = {
        "wishlist": True,
        "wishlist_items": wishlist_items,
    }

    return render(request,
                  template,
                  context)


def add_to_wishlist(request, item_id):
    # item = get_object_or_404(Item, pk=item_id)

    wishlist = request.session.get("wishlist", {})
    redirect_url = request.POST.get("redirect_url")

    wishlist[item_id] = item_id
    request.session["wishlist"] = wishlist
    item = get_object_or_404(Item, pk=item_id)
    # return redirect(redirect_url)
    messages.success(request,
                     f"{item.name} has been added to your wishlist.")
    return HttpResponse(status=200)
