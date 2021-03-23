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
        self.update_cart = reverse("update_cart",
                                   kwargs={"item_id": self.item.id})

    def test_view_cart_view_GET(self):
        ''' test the view cart page  '''

        response = self.client.get(self.view_cart)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart/cart.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "includes/nav-background.html")

    def test_add_to_cart_GET(self):
        ''' test that id the url is typed
        into the browser the user is redirected
        and an error message is shown  '''

        response = self.client.get(self.add_to_cart)
        self.assertRedirects(response, self.home_page)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Error you do not have permission to do this.")

    def test_add_to_cart_POST(self):
        ''' test that an item is added to the
         cart and then context is then updated and
         then if the item is added a second time the quantity is updated '''

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
        # test that adding the item again updates the quantity
        response = self.client.post(self.add_to_cart,
                                    data={"quantity": 1,
                                          "redirect_url": "/"})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "test item's quantity has been updated to 2")

    def test_update_cart_GET(self):
        ''' test that if the url is type in
        the user is redirected and an error message is shown '''

        response = self.client.get(self.update_cart)
        self.assertRedirects(response, self.home_page)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Error you do not have permission to do this.")

    def test_update_cart_POST(self):
        ''' test the cart is updated upon posting a new quantity
        and if the quantity is set to 0 the item is removed '''

        response = self.client.post(self.update_cart,
                                    data={"item_quantity": 2})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "test item's  quantity has been updated to 2")
        response = self.client.post(self.view_cart)
        context = response.context
        self.assertNotEqual(context["cart_items"], [])
        self.assertEqual(context["cart_items"][0]["quantity"], 2)

        # test cart empties when quantity set to 0
        response = self.client.post(self.update_cart,
                                    data={"item_quantity": 0})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "test item has been removed from your cart.")
        response = self.client.post(self.view_cart)
        context = response.context
        self.assertEqual(context["cart_items"], [])
