from django.test import SimpleTestCase
from django.urls import reverse, resolve
from reviews.views import our_reviews, edit_review, delete_review


class TestReviewsUrls(SimpleTestCase):

    def test_our_reviews_ure(self):
        url = reverse("our_reviews")
        self.assertEquals(resolve(url).func, our_reviews)

    def test_edit_review_url(self):
        url = reverse("edit_review", args=["1"])
        self.assertEquals(resolve(url).func, edit_review)

    def test_delete_review_url(self):
        url = reverse("delete_review", args=["1"])
        self.assertEquals(resolve(url).func, delete_review)
