from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = (
        "lineitem_total",
    )


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        "order_number",
        "date",
        "home_delivery_cost",
        "order_total",
        "grand_total",
        "original_cart",
        "stripe_payment_intent_id",
    )

    fields = (
        "order_number",
        "user_profile",
        "full_name",
        "email",
        "contact_number",
        "street_address_1",
        "street_address_2",
        "town_or_city",
        "county",
        "eircode",
        "country",
        "date",
        "home_delivery_cost",
        "order_total",
        "grand_total",
        "original_cart",
        "stripe_payment_intent_id",
    )

    list_display = (
        "order_number",
        "date",
        "full_name",
        "order_total",
        "home_delivery_cost",
        "grand_total",
    )

    ordering = (
        "-date",
    )


admin.site.register(Order, OrderAdmin)
