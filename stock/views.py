from django.shortcuts import render, get_object_or_404
from .models import Item


def all_items(request):
    ''' Shows all items page  '''

    items = Item.objects.all()

    template = "stock/all_items.html"

    context = {
        "items": items
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
