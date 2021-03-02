from django.shortcuts import (render, get_object_or_404,
                              reverse)
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Item


def all_items(request):
    ''' Shows all items page, The view gets all items
    form the database and then uses Django paginator to paginate them.
    It then handles the search queries from the navigation,
    using the django Q object to filter the results.
    '''

    items = Item.objects.all()
    search = None

    if request.GET and "query" in request.GET:
        search = request.GET["query"]
        if not search:
            messages.error(request, "No search query entered.")

        search_items = Q(name__icontains=search) \
            | Q(description__icontains=search)
        items = items.filter(search_items)

    template = "stock/all_items.html"

    paginator = Paginator(items, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
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
