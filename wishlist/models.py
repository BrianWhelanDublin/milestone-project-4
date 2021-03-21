from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UsersWishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wishlist = models.TextField(null=False, blank=False, default="")

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_the_user_wishlist(sender, instance, created,
                                       **kwargs):
    if created:
        UsersWishlist.objects.create(user=instance)
    instance.userprofile.save()
