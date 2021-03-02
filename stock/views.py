from django.shortcuts import (render, get_object_or_404,
                              reverse, redirect)
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator
from .models import Item, Category


def all_items(request):
    ''' Shows all items page, The view gets all items
    form the database and then uses Django paginator to paginate them.
    It then handles the search queries from the navigation,
    using the django Q object to filter the results.
    '''

    items = Item.objects.all()
    search = None
    category = None
    current_category = None
    sort = None
    direction = None

    if request.GET and "sort" in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if sortkey == "name":
            items = items.annotate(sortkey=Lower("name"))
        if "direction" in request.GET:
            direction = request.GET["direction"]
            if direction == 'desc':
                sortkey = f"-{sortkey}"
        if sortkey == "None":
            items = items
        else:
            items = items.order_by(sortkey)

    if request.GET and "query" in request.GET:
        search = request.GET["query"]
        if not search:
            messages.error(request, "No search query entered.")
            return redirect(reverse("all_items"))

        search_items = Q(name__icontains=search) \
            | Q(description__icontains=search)
        items = items.filter(search_items)

    if request.GET and "category" in request.GET:
        category = request.GET["category"]
        items = items.filter(category__name=category)
        current_category = get_object_or_404(Category, name=category)

    template = "stock/all_items.html"

    paginator = Paginator(items, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    current_sorting = f"{sort}_{direction}"

    context = {
        "page_obj": page_obj,
        "search": search,
        "current_category": current_category,
        "current_sorting": current_sorting,
        "sort": sort,
        "direction": direction,
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
