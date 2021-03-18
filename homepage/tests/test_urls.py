from django.test import SimpleTestCase
from django.urls import reverse, resolve
from homepage.views import home_page, our_story, contact


class TestUrls(SimpleTestCase):

    def test_home_page_url(self):
        url = reverse("home_page")
        self.assertEquals(resolve(url).func, home_page)

    def test_our_story_url(self):
        url = reverse("our_story")
        self.assertEquals(resolve(url).func, our_story)

    def test_contact_url(self):
        url = reverse("contact")
        self.assertEquals(resolve(url).func, contact)
