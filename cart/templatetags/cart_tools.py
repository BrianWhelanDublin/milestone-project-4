from django import template


register = template.Library()


@register.filter(name="calculate_total")
def calculate_total(price, quantity):
    return price * quantity
