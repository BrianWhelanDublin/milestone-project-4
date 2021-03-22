from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cart.views import view_cart, update_cart, remove_from_cart, add_to_cart


class TestCartUrls(SimpleTestCase):

    def test_view_cart_url(self):
        url = reverse("view_cart")
        self.assertEquals(resolve(url).func, view_cart)

    def test_add_cart_url(self):
        url = reverse("add_to_cart", args=["1"])
        self.assertEquals(resolve(url).func, add_to_cart)

    def test_update_cart_url(self):
        url = reverse("update_cart", args=["1"])
        self.assertEquals(resolve(url).func, update_cart)

    def test_remove_cart_url(self):
        url = reverse("remove_from_cart", args=["1"])
        self.assertEquals(resolve(url).func, remove_from_cart)
