from django.test import TestCase, Client
from django.urls import reverse
from reviews.forms import ReviewForm
from reviews.models import Review
from django.contrib.auth.models import User
from django.contrib.messages import get_messages


class TestReviewViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.our_reviews = reverse("our_reviews")
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testPassword'
        )
        self.user2 = User.objects.create_user(
            username='testuser2',
            email='test2@email.com',
            password='test2Password'
        )
        self.review2 = Review.objects.create(
            reviewer=self.user2,
            review="Test Review 2",
            stars="5",
        )
        self.edit_review = reverse("edit_review",
                                   kwargs={"review_id": self.review2.id})

    def test_our_reviews_GET(self):
        ''' test the our reviews page get '''

        response = self.client.get(self.our_reviews)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reviews/our_reviews.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "includes/nav-background.html")

    def test_view_reviews_POST_form_valid(self):
        ''' test the view post view with a get request
            and a valid form '''

        self.client.login(
            username="testuser", password="testPassword")
        self.client.post(self.our_reviews,
                         {"review": "Test Review",
                          "stars": "5"})
        review = Review.objects.get(reviewer=self.user)
        self.assertTrue(review)
        self.assertEqual(review.review, 'Test Review')
        self.assertEqual(review.stars, 5)

    def test_edit_post_if_not_reviewer(self):
        ''' test the edit post view if a user isnt a superuser '''

        self.client.login(
            username="testuser", password="testPassword")
        response = self.client.get(self.edit_review)
        self.assertRedirects(response, self.our_reviews)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "You do not have permission to do this.")

