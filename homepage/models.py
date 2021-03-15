from django.db import models


class NewsletterSubscriber(models.Model):

    email = models.EmailField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.email


class Message(models.Model):
    subject = models.CharField(max_length=100, null=False, blank=False)
    user_email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.subject
