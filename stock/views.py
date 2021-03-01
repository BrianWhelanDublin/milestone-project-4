from django.shortcuts import (render, get_object_or_404,
                              reverse)
from django.contrib import messages
from django.db.models import Q
from .models import Item


def all_items(request):
    ''' Shows all items page  '''

    items = Item.objects.all()
    search = None

    ''' Handles the search queries from the navigation,
    using the django Q object to filter the results '''
    if request.GET:
        if "query" in request.GET:
            search = request.GET["query"]
        if not search:
            messages.error(request, "No search query entered.")

        search_items = Q(name__icontains=search) \
            | Q(description__icontains=search)
        items = items.filter(search_items)

    template = "stock/all_items.html"

    context = {
        "items": items,
        "search": search,
    }

    return render(request,
                  template,
                  context)


def single_item(request, item_id):
    ''' Shows the single item page '''

    item = get_object_or_404(Item, pk=item_id)

    template = "stock/item.html"

    context = {
        "item": item
    }

    return render(request,
                  template,
                  context)
