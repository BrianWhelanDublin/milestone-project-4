from django.contrib import admin
from .models import NewsletterSubscriber, Message


class NewsletterSubscriberAdmin(admin.ModelAdmin):
    model = NewsletterSubscriber
    list_display = (
        "email",
    )


class MessageAdmin(admin.ModelAdmin):
    model = Message
    readonly_fields = (
        "subject",
        "user_email",
        "message",
    )


admin.site.register(NewsletterSubscriber,
                    NewsletterSubscriberAdmin)
admin.site.register(Message, MessageAdmin)
