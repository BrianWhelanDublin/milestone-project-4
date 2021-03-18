from django.test import TestCase
from homepage.models import Message, NewsletterSubscriber


class TestHomepageModels(TestCase):

    def test_newsletter_model(self):
        subscriber = NewsletterSubscriber.objects.create(
            email="test@email.com")
        self.assertEqual(str(subscriber), "test@email.com")

    def test_message_model(self):
        message = Message.objects.create(
            subject="test",
            user_email="test@email.com",
            message="Test message"
            )

        self.assertEqual(str(message), "test")
