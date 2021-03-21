from django.contrib import admin
from .models import UsersWishlist


class UsersWishlistAdmin(admin.ModelAdmin):
    model = UsersWishlist
    list_display = (
        "user",
    )


admin.site.register(UsersWishlist, UsersWishlistAdmin)
