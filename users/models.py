from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_contact_number = models.CharField(max_length=20,
                                           null=True, blank=True)
    user_street_address_1 = models.CharField(max_length=80,
                                             null=True, blank=True)
    user_street_address_2 = models.CharField(max_length=80,
                                             null=True, blank=True)
    user_town_or_city = models.CharField(max_length=50,
                                         null=True, blank=True)
    user_county = models.CharField(max_length=50,
                                   null=True, blank=True)
    user_eircode = models.CharField(max_length=10,
                                    null=True, blank=True)
    user_country = CountryField(blank_label="Country",
                                null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_the_userprofile(sender, instance, created, **kwargs):
    ''' creates the user profile or updates it if there is one already '''

    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
