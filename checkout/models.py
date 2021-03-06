from django.db import models
from django.db.models import Sum
from django.conf import settings

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


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete="models.CASCADE",
                              related_name="lineitems")
    item = models.ForeignKey(Item, null=False, blank=False,
                             on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False)
