from django.test import SimpleTestCase
from django.urls import reverse, resolve
from stock.views import (all_items, single_item,
                         add_item, edit_item, delete_item)


class TestUrls(SimpleTestCase):

    def test_all_items_url(self):
        url = reverse("all_items")
        self.assertEquals(resolve(url).func, all_items)

    def test_single_item_url(self):
        url = reverse("single_item", args=["1"])
        self.assertEquals(resolve(url).func, single_item)

    def test_add_item_url(self):
        url = reverse("add_item")
        self.assertEquals(resolve(url).func, add_item)

    def test_edit_item_url(self):
        url = reverse("edit_item", args=["1"])
        self.assertEquals(resolve(url).func, edit_item)

    def test_delete_item_url(self):
        url = reverse("delete_item", args=["1"])
        self.assertEquals(resolve(url).func, delete_item)
