from django import template
from stock.models import Item
from django.shortcuts import get_object_or_404


register = template.Library()


@register.filter(name='ifinlist')
def ifinlist(value, list):
    item = get_object_or_404(Item, pk=value)
    if item in list:
        return True
