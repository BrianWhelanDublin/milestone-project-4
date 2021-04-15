from django.test import TestCase
from checkout import apps


class CheckoutAppTests(TestCase):

    def test_apps_config(self):
        """ test blog app configured correctly"""

        self.assertEqual(apps.CheckoutConfig.name, 'checkout')
