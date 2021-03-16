from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    review = models.TextField(null=False, blank=False)
    stars = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.review
