from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import user_profile, previous_order


class TestUserUrls(SimpleTestCase):

    def test_user_profile_url(self):
        url = reverse("user_profile")
        self.assertEquals(resolve(url).func, user_profile)

    def test_previous_order_url(self):
        url = reverse("previous_order", args=["1"])
        self.assertEquals(resolve(url).func, previous_order)
