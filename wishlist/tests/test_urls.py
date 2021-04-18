from django.test import SimpleTestCase
from django.urls import reverse, resolve
from wishlist.views import (view_wishlist, remove_from_wishlist,
                            add_to_wishlist, delete_wishlist)


class TestUrls(SimpleTestCase):

    def test_view_wishlist_url(self):
        url = reverse("view_wishlist")
        self.assertEquals(resolve(url).func, view_wishlist)

    def test_remove_from_wishlist_url(self):
        url = reverse("remove_from_wishlist", args=["1"])
        self.assertEquals(resolve(url).func, remove_from_wishlist)

    def test_add_to_wishlist_url(self):
        url = reverse("add_to_wishlist", args=["1"])
        self.assertEquals(resolve(url).func, add_to_wishlist)

    def test_delete_wishlist_url(self):
        url = reverse("delete_wishlist")
        self.assertEquals(resolve(url).func, delete_wishlist)
