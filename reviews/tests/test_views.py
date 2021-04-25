from django.test import TestCase, Client
from django.urls import reverse
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
            stars=5,
        )
        self.edit_review = reverse("edit_review",
                                   kwargs={"review_id": self.review2.id})
        self.delete_review = reverse("delete_review",
                                     kwargs={"review_id": self.review2.id})

    def test_our_reviews_GET(self):
        ''' test the our reviews page GET '''

        response = self.client.get(self.our_reviews)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reviews/our_reviews.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "includes/nav-background.html")

    def test_view_reviews_POST_form_valid(self):
        ''' test the view reviews view with a GET request
        '''

        self.client.login(
            username="testuser", password="testPassword")
        self.client.post(self.our_reviews,
                         {"review": "Test Review",
                          "stars": 5})
        review = Review.objects.get(reviewer=self.user)
        self.assertTrue(review)
        self.assertEqual(review.review, 'Test Review')
        self.assertEqual(review.stars, 5)

    def test_edit_review_GET_if_not_reviewer(self):
        ''' test the edit review view if the user didn't
            write the review '''

        self.client.login(
            username="testuser", password="testPassword")
        response = self.client.get(self.edit_review)
        self.assertRedirects(response, self.our_reviews)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "You do not have permission to do this.")

    def test_edit_review_GET_if_reviewer(self):
        ''' test the edit review if the user wrote the review '''

        self.client.login(
            username="testuser2", password="test2Password")
        response = self.client.get(self.edit_review)
        self.assertEqual(response.context['form'].initial['review'],
                         self.review2.review)
        self.assertEqual(response.context['form'].initial['stars'],
                         self.review2.stars)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reviews/our_reviews.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "includes/nav-background.html")

    def test_edit_review_POST_invalidform(self):
        ''' test the edit review POST with an invalid form'''

        self.client.login(
            username="testuser2", password="test2Password")

        response = self.client.post(self.edit_review, {

        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Failed to update review. Please try again later.")

    def test_edit_review_POST_validform(self):
        ''' test the edit review POST with a valid form '''

        self.client.login(
            username="testuser2", password="test2Password")

        response = self.client.post(self.edit_review, {
            "review": "Test Review Edited",
            "stars": 4,
            }
        )
        review = Review.objects.get(id=self.review2.id)
        self.assertEqual(review.review, 'Test Review Edited')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Review has been updated.")

    def test_delete_review_if_not_reviewer(self):
        ''' test the delete post view if a user isnt the reviewer'''

        self.client.login(
            username="testuser", password="testPassword")

        response = self.client.post(self.delete_review)
        self.assertRedirects(response, self.our_reviews)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "You do not have permission to do this.")

    def test_delete_post_GET_if_reviewer(self):
        ''' test the delete post view GET '''

        self.client.login(
            username="testuser2", password="test2Password")
        response = self.client.get(self.delete_review)
        self.assertRedirects(response, self.our_reviews)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "You do not have permission to do this.")

    def test_delete_review_POST(self):
        ''' Test the delete review POST function '''

        self.client.login(
            username="testuser2", password="test2Password")
        response = self.client.post(self.delete_review)
        review = Review.objects.filter(id=self.review2.id)
        self.assertFalse(review)
        self.assertRedirects(response, self.our_reviews)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Review has been deleted")
