from django.test import TestCase, Client
from django.urls import reverse
from stock.models import Item
from django.contrib.auth.models import User
from django.contrib.messages import get_messages


class TestCartViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_page = reverse("home_page")
        self.view_cart = reverse("view_cart")
        self.item = Item.objects.create(name="test item", price="1")
        self.add_to_cart = reverse("add_to_cart",
                                   kwargs={"item_id": self.item.id})

    def test_view_cart_view_GET(self):
        response = self.client.get(self.view_cart)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart/cart.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "includes/nav-background.html")

    def test_add_to_cart_GET(self):
        response = self.client.get(self.add_to_cart)
        self.assertRedirects(response, self.home_page)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Error you do not have permission to do this.")

    def test_add_to_cart_POST(self):
        response = self.client.post(self.add_to_cart,
                                    data={"quantity": "1",
                                          "redirect_url": "/"})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "test item has been added to your cart.")
        response = self.client.post(self.view_cart)
        context = response.context
        self.assertNotEqual(context["cart_items"], [])
        self.assertEqual(context["cart_items"][0]["item_id"],
                         f"{self.item.id}")
