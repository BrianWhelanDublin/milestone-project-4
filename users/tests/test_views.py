from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from users.forms import UserProfileForm
from users.models import UserProfile
from checkout.models import Order


class TestUserViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.user_profile = reverse("user_profile")
        self.login = reverse("account_login")
        self.form = UserProfileForm

    def test_user_profile_login_required(self):
        ''' Test the user needs to be logged in to see the userprofile page '''

        response = self.client.get(self.user_profile)
        self.assertNotEqual(response.status_code, 200)

    def test_user_profile_page_logged_in(self):
        ''' Test the user profile page when logged in '''

        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(self.user_profile)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/user_profile.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "includes/nav-background.html")

    def test_user_profile_post_error(self):
        ''' Test if form filled out incorrectly '''

        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(self.user_profile, {
            "user_eircode": "0808876567889998765543345677"}
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Your detials can't be save. \
 Please check your form is filled out correctly.")

    def test_user_profile_post_valid_form(self):
        ''' Test if from is valid '''

        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(self.user_profile, {
            "user_contact_number": "087222222",
            "user_street_address_1": "59",
            "user_street_address_2": "main st",
            "user_town_or_city": "dublin",
            "user_county": "dublin",
            "user_eircode": "d22"}
        )
        form = self.form(response, instance=self.user)
        self.assertTrue(form.is_valid())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Your profile has been updated successfully.")

    def test_previous_orders_view_unloggedin(self):
        ''' Test view of previous orders not logged in '''

        user_profile = UserProfile.objects.get(user=self.user)
        order = Order.objects.create(user_profile=user_profile)
        response = self.client.get(
            reverse("previous_order",
                    kwargs={"order_number": order.order_number}))
        self.assertEqual(response.status_code, 302)

    def test_previous_orders_view(self):
        ''' Test previous orders view with logged in user '''

        self.client.login(username="testuser", password="testpassword")
        user_profile = UserProfile.objects.get(user=self.user)

        order = Order.objects.create(user_profile=user_profile)

        response = self.client.get(
            reverse("previous_order",
                    kwargs={"order_number": order.order_number}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/checkout_success.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "includes/nav-background.html")
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "This is a previous order")
