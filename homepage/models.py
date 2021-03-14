from django.db import models


class NewsletterSubscriber(models.Model):

    email = models.EmailField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.email
