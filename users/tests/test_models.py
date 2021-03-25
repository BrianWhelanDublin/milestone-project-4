from django.test import TestCase, Client
from users.models import UserProfile
from django.contrib.auth.models import User


class TestUserProfileModel(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )

    def test_userprofile_model(self):
        self.client.login(username="testuser", password="testpassword")
        user_profile = UserProfile.objects.get(
            user=self.user,
        )
        self.assertEqual(str(user_profile), self.user.username)
