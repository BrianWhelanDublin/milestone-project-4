from django.test import TestCase, Client
from reviews.models import Review
from django.contrib.auth.models import User


class TestReviewsModels(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )

    def test_review_model(self):
        review = Review.objects.create(
            reviewer=self.user,
            review="Test Review",
            stars="5",
        )
        self.assertEqual(str(review), "Test Review")
