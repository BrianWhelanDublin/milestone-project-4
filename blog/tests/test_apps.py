from django.test import TestCase
from blog import apps


class BlogAppTests(TestCase):

    def test_apps_config(self):
        """ test blog app configured correctly"""

        self.assertEqual(apps.BlogConfig.name, 'blog')
