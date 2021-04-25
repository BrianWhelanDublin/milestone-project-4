from django.test import TestCase
from homepage.forms import NewsletterForm, MessageForm


class TestNewsletterForm(TestCase):

    def test_email_is_required(self):
        form = NewsletterForm({
            "email": ""
        })
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors.keys())
        self.assertEqual(form.errors["email"][0], "This field is required.")


class TestMessageForm(TestCase):

    def setUp(self):
        self.form = MessageForm({
            "name": "",
            "user_email": "",
            "message": "",
        })

    def test_subject_is_required(self):
        form = self.form
        self.assertFalse(form.is_valid())
        self.assertIn("subject", form.errors.keys())
        self.assertEqual(form.errors["subject"][0], "This field is required.")

    def test_user_email_is_required(self):
        form = self.form
        self.assertFalse(form.is_valid())
        self.assertIn("user_email", form.errors.keys())
        self.assertEqual(form.errors["user_email"][0],
                         "This field is required.")

    def test_message_is_required(self):
        form = self.form
        self.assertFalse(form.is_valid())
        self.assertIn("message", form.errors.keys())
        self.assertEqual(form.errors["message"][0], "This field is required.")

    def test_form_fields(self):
        form = MessageForm()
        fields = []
        for field in form.fields:
            fields.append(field)
            print(field)
        self.assertEqual(fields,
                         ["subject", "user_email", "message"])
