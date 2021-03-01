from django.shortcuts import render
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
