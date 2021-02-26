from django.contrib import admin
from .models import Category, Item


# Register Item and Category models.
admin.site.register(Item)
admin.site.register(Category)
