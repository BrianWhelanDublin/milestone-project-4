from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from wishlist.models import UsersWishlist
from stock.models import Item


class TestWishlistModels(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.item = Item.objects.create(name="test item", price=99.99)
        self.view_wishlist = reverse("view_wishlist")
        self.add_to_wishlist = reverse("add_to_wishlist",
                                       kwargs={"item_id": self.item.id})
        self.remove_from_wishlist = reverse("remove_from_wishlist",
                                            kwargs={"item_id": self.item.id})
        self.delete_wishlist = reverse("delete_wishlist")
        self.all_items = reverse("all_items")
        self.home_page = reverse("home_page")

    def test_view_wishlist_GET(self):
        ''' Test the view wishlist view '''

        response = self.client.get(self.view_wishlist)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "wishlist/wishlist.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "includes/nav-background.html")

    def test_add_to_wishlist_GET(self):
        ''' Test the add to wishlist view GET request '''

        response = self.client.get(self.add_to_wishlist)
        self.assertRedirects(response, self.all_items)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "You do not have permission to do this.")

    def test_add_to_wishlist_POST(self):
        ''' Test the add to wishlist view POST request '''

        self.client.login(
            username="testuser", password="testpassword")
        response = self.client.post(self.add_to_wishlist)
        wishlist = UsersWishlist.objects.get(user=self.user)
        items = wishlist.items.all()
        self.assertTrue(items[0], self.item)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         f"{self.item.name} has been added to your wishlist.")

    def test_remove_from_wishlist_GET(self):
        ''' Test the remove from wishlist view GET request '''

        response = self.client.get(self.remove_from_wishlist)
        self.assertRedirects(response, self.home_page)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Error you do not have \
permission to do this.")

    def test_remove_from_wishlist_POST(self):
        ''' Test the remove from wishlist view POST request '''

        self.client.login(
            username="testuser", password="testpassword")
        self.client.post(self.add_to_wishlist)
        response = self.client.post(self.remove_from_wishlist)
        wishlist = UsersWishlist.objects.get(user=self.user)
        items = wishlist.items.all()
        self.assertFalse(items)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 2)
        self.assertEqual(str(messages[1]),
                         f"{self.item.name} has been removed \
 from your wishlist.")

    def test_delete_wishlist_GET(self):
        ''' Test the delete wishlist view GET request '''

        response = self.client.get(self.delete_wishlist)
        self.assertRedirects(response, self.home_page)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Error you do not have \
permission to do this.")

    def test_delete_wishlist_POST(self):
        ''' Test the delete wishlist view POST request '''

        self.client.login(
            username="testuser", password="testpassword")
        self.client.post(self.add_to_wishlist)

        response = self.client.post(self.delete_wishlist)
        wishlist = UsersWishlist.objects.get(user=self.user)
        items = wishlist.items.all()
        self.assertFalse(items)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 2)
        self.assertEqual(str(messages[1]),
                         "Your wishlist has been deleted.")
