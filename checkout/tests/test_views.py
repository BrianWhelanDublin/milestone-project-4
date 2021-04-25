from django.test import TestCase, Client
from django.urls import reverse
from stock.models import Item
from django.contrib.auth.models import User
from django.contrib.messages import get_messages


class TestCheckoutViews(TestCase):

    def setUp(self):

        self.client = Client()
        self.checkout = reverse("checkout")
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testPassword'
        )
        self.item = Item.objects.create(name="test item", price="1")
        self.add_to_cart = reverse("add_to_cart",
                                   kwargs={"item_id": self.item.id})

    def test_checkout_view_with_empty_cart(self):
        ''' Test the checkout view with an empty cart. '''

        response = self.client.get(self.checkout)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Your cart is currently empty.")

    def test_checkout_view_with_cart(self):
        ''' Test the checkout view with a =n item in the cart '''

        self.client.post(self.add_to_cart,
                         data={"quantity": "1",
                               "redirect_url": "/"})
        response = self.client.get(self.checkout)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/checkout.html")
        self.assertTemplateUsed(response, "base.html")

    def test_checkout_success(self):
        ''' Test the checkout success view. '''

        self.client.post(self.add_to_cart,
                         data={"quantity": "1",
                               "redirect_url": "/"})
        response = self.client.post(self.checkout,
                                    data={
                                        'full_name': 'testuser',
                                        'email': 'test@email.com',
                                        'contact_number': '0873534365',
                                        'street_address_1': 'main st',
                                        'street_address_2': '',
                                        'town_or_city': 'dublin',
                                        'county': 'dublin',
                                        'country': 'IE',
                                        'eircode': '',
                                        'client_secret': 'client',
                                    }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')

    def test_checkout_view_with_form_prefilled(self):
        ''' Test the checkout view form is prefilled
            With the user data'''

        self.client.post(self.add_to_cart,
                         data={"quantity": "1",
                               "redirect_url": "/"})
        self.client.login(username="testuser", password="testPassword")
        response = self.client.get(self.checkout)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].initial['email'],
                         self.user.email)
