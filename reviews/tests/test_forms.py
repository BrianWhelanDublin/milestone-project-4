from django.test import TestCase
from reviews.forms import ReviewForm


class TestReviewForm(TestCase):

    def test_review_is_required(self):
        form = ReviewForm({
            "review": ""
        })
        self.assertFalse(form.is_valid())
        self.assertIn("review", form.errors.keys())
        self.assertEqual(form.errors["review"][0], "This field is required.")

    def test_stars_are_required(self):
        form = ReviewForm({
            "stars": ""
        })
        self.assertFalse(form.is_valid())
        self.assertIn("stars", form.errors.keys())
        self.assertEqual(form.errors["stars"][0], "This field is required.")

    def test_form_fields(self):
        form = ReviewForm()
        fields = []
        for field in form.fields:
            fields.append(field)
            print(field)
        self.assertEqual(fields,
                         ["review", "stars"])
