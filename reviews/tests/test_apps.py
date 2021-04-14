from django.test import TestCase
from reviews import apps


class ReviewAppTests(TestCase):

    def test_apps_config(self):
        """ test blog app configured correctly"""
        self.assertEqual(apps.ReviewsConfig.name, 'reviews')
