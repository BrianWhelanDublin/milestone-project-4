from django.db import models
from django.db.models import Sum
from django.conf import settings

from decimal import Decimal

import uuid

from stock.models import Item


class Order(models.Model):
    ''' Create the order model '''

    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    contact_number = models.CharField(max_length=20, null=False, blank=False)
    street_address_1 = models.CharField(max_length=80, null=False, blank=False)
    street_address_2 = models.CharField(max_length=80, null=False, blank=False)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    county = models.CharField(max_length=50, null=False, blank=False)
    eircode = models.CharField(max_length=10, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    home_delivery_cost = models.DecimalField(max_digits=6,
                                             decimal_places=2,
                                             null=False, default=0)
    order_total = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      null=False, default=0)
    subtotal = models.DecimalField(max_digits=6,
                                   decimal_places=2,
                                   null=False, default=0)

    # model methods
    def _create_order_number(self):
        ''' Uses UUID to generate a random order number '''
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        ''' Override the original save method to save an order number '''

        if not self.order_number:
            self.order_number = self._create_order_number()
        super().save(*args, **kwargs)

    def update_subtotal(self):
        ''' Update the subtotal each time a new line item is added '''

        self.order_total = self.lineitems.aggregate(
            Sum("lineitem_total"))["lineitem_total__sum"] or 0

        delivery_cost = self.order_total * Decimal(
            settings.DELIVERY_COST_PERCENTAGE/100)
        if delivery_cost < settings.STANDARD_HOME_DELIVERY_COST_MIN:
            self.home_delivery_cost = settings.STANDARD_HOME_DELIVERY_COST_MIN
        elif delivery_cost > settings.STANDARD_HOME_DELIVERY_COST_MAX:
            self.home_delivery_cost = settings.STANDARD_HOME_DELIVERY_COST_MAX
        else:
            self.home_delivery_cost = delivery_cost
        self.subtotal = self.order_total + self.home_delivery_cost
        self.save()

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name="lineitems")
    item = models.ForeignKey(Item, null=False, blank=False,
                             on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False)

    def save(self, *args, **kwargs):
        ''' overrides the origanl save to set lineitem total '''

        self.lineitem_total = self.item.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Code: {self.item.code} on order {self.order.order_number}"
