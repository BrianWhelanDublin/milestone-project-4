from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    readonly_fields = (
        "reviewer",
        "review",
        "message",
    )
