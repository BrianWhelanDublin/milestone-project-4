from django.test import TestCase, Client
from django.urls import reverse
from homepage.forms import MessageForm
from users.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.messages import get_messages


class TestHomepageViews(TestCase):

    def setUp(self):

        self.client = Client()
        self.home_page = reverse("home_page")
        self.our_story = reverse("our_story")
        self.contact = reverse("contact")
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testPassword'
        )

    def test_homepage_view_GET(self):
        ''' Test the home page view '''

        response = self.client.get(self.home_page)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "homepage/index.html")
        self.assertTemplateUsed(response, "base.html")

    def test_newsletter_signup_POST(self):
        ''' Test the newsletter sign up '''

        response = self.client.post(self.home_page,
                                    {"email": "test@email.com"})
        self.assertRedirects(response, self.home_page)

    def test_newsletter_signup_error(self):
        ''' test if there was an error on signing up for the newsletter '''

        response = self.client.post(self.home_page,
                                    {"email": ""})
        self.assertRedirects(response,
                             self.home_page)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Something has gone wrong.\
 Please check your email address and try again.")

    def test_contact_page_view_on_get(self):
        ''' Test the contact page on opening '''

        response = self.client.get(self.contact)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "homepage/contact.html")
        self.assertTemplateUsed(response, "includes/nav-background.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTrue(response.context['form'], MessageForm)

    def test_contact_email_is_prefilled_for_loggedin_user(self):
        ''' test that when a user is logged in the
         email form is prefilled with their email from their userprofile '''

        self.client.login(username="testuser", password="testPassword")
        user_profle = UserProfile.objects.get(user=self.user)
        response = self.client.get(self.contact)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].initial['user_email'],
                         user_profle.user.email)

    def test_contact_email_is_prefilled_error(self):
        '''  Test the exception if the Userprofile isnt found.'''

        self.client.login(username="testuser",
                          password="testPassword")
        response = self.client.get(self.contact)
        UserProfile(user=None)
        self.assertTrue(response.context['form'], MessageForm)

    def test_contact_POST(self):
        ''' test the POST view of the contact '''

        response = self.client.post(self.contact, {
            "subject": "test",
            "user_email": "test@email.com",
            "message": "test"
        })
        self.assertRedirects(response, self.home_page)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Your message has been sent.\
 A member of our customer service team will be in contact soon.")

    def test_contact_error(self):
        ''' test if there was an error with the posting '''

        response = self.client.post(self.contact, {
            "subject": "",
            "user_email": "",
            "message": ""
        })
        self.assertRedirects(response, self.contact)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Something has gone wrong.\
 Please try again soon")

    def test_our_story_view_GET(self):
        ''' Test the our story view '''

        response = self.client.get(self.our_story)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "homepage/our_story.html")
        self.assertTemplateUsed(response, "includes/nav-background.html")
        self.assertTemplateUsed(response, "base.html")
