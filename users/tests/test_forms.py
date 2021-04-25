from django.test import TestCase, Client
from users.forms import UserProfileForm
from django.contrib.auth.models import User


class TestUserProfileForm(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testPassword'
        )
        self.form = UserProfileForm

    def test_form_meta_fields(self):
        form = self.form({
            "user": self.user,
            "user_contact_number": "Contact Number",
            "user_street_address_1": "Address",
            "user_street_address_2": "Address",
            "user_town_or_city": "Town or City",
            "user_county": "County",
            "user_eircode": "Eircode",
        })
        self.assertTrue(form.is_valid())

    def test_fields_are_not_required(self):
        form = self.form({})
        self.assertTrue(form.is_valid())
