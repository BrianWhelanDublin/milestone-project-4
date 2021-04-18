from django.test import TestCase, Client
from wishlist.models import UsersWishlist
from django.contrib.auth.models import User


class UsersWishlistModedl(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )

    def test_usewishlist_model(self):
        user_wishlist = UsersWishlist.objects.get(user=self.user)
        self.assertEqual(str(user_wishlist), self.user.username)
