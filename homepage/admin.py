from django.contrib import admin
from .models import NewsletterSubscriber


class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = (
        "email",
    )


admin.site.register(NewsletterSubscriber,
                    NewsletterSubscriberAdmin)
