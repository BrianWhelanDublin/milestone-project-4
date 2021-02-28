from django.shortcuts import render
from stock.models import Item


def home_page(request):
    ''' retrieve the new items from the databse,
        then render the homepage'''

    new_items = Item.objects.filter(category=7)

    template = "homepage/index.html"
    context = {
        "new_items": new_items
    }

    return render(request,
                  template,
                  context)


def our_story(request):
    ''' render our story page '''

    template = "homepage/our_story.html"

    return render(request,
                  template)
