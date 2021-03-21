from django.db import models
from django.contrib.auth.models import User
from stock.models import Item

from django.db.models.signals import post_save
from django.dispatch import receiver


class UsersWishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_the_UserWishlist(sender, instance, created, **kwargs):
    ''' creates the user profile or updates it if there is one already '''
    if created:
        UsersWishlist.objects.create(user=instance)
    instance.userprofile.save()
