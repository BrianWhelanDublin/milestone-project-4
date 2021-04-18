from django.test import TestCase
from stock import apps


class StockAppTests(TestCase):

    def test_apps_config(self):
        """ test blog app configured correctly"""

        self.assertEqual(apps.StockConfig.name, 'stock')
