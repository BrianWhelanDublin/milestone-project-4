from django import template


register = template.Library()


@register.filter(name='ifinlist')
def ifinlist(value, list):
    key = "item_id"
    for item in list:
        if item[key] == str(value):
            return True
