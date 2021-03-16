from django.db import models
from users.models import UserProfile


class Review(models.Model):
    reviewer = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 related_name="reviews")
    review = models.TextField(null=False, blank=False)
    stars = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.review
