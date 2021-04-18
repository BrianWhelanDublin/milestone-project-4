from django.test import TestCase
from wishlist import apps


class WishlistAppTests(TestCase):

    def test_apps_config(self):
        """ test wishlist app"""

        self.assertEqual(apps.WishlistConfig.name, 'wishlist')
